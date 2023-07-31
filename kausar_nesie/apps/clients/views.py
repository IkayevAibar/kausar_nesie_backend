from django.db.models import Q, Count

from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend , CharFilter
from django_filters import FilterSet, DateTimeFromToRangeFilter

# from excel_response import ExcelResponse
from django_excel_response import ExcelResponse

from .serializers import *
from .models import *


class IndividualClientViewSet(viewsets.ModelViewSet):
    """Физические лица"""
    queryset = IndividualClient.objects.all()
    serializer_class = IndividualClientSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        # Используем IndividualClientReadOnlySerializer для чтения
        if self.action == 'list' or self.action == 'retrieve':
            return IndividualClientRetrieveSerializer
        return self.serializer_class


class AddressViewSet(viewsets.ModelViewSet):
    """Адреса клиента"""
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AddressRetrieveSerializer
        return self.serializer_class

class ClientFilter(FilterSet):
    individual_client__rnn = CharFilter()
    individual_client__iin = CharFilter()
    individual_client__full_name = CharFilter()
    class Meta:
        model = Client
        fields = ['individual_client__rnn','individual_client__iin', 'individual_client__full_name', 'individual_client__gender', 'individual_client__is_resident', 'individual_client__country', \
    'individual_client__client_category']


class ClientViewSet(viewsets.ModelViewSet):
    """Клиент"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = ClientFilter

    # search_fields = ['individual_client__reg_number', 'individual_client__iin', '^individual_client__full_name', '=individual_client__full_name', \
    #     'individual_client__full_name',]
    # filterset_fields = ['individual_client__gender', 'individual_client__is_resident', 'individual_client__country', \
    #     'individual_client__client_category']

    pagination_class = None

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Instead of returning the full serialized data, return only the 'id' field
        return Response({'client_id': serializer.instance.id}, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def add_balance_to_account(self, request, pk=None):
        client = self.get_object()

        try:
            amount = request.data['amount']
        except KeyError:
            return Response({'error': 'amount не указан'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            account = Account.objects.get(client=client)
        except Account.DoesNotExist:
            return Response({'error': 'Счёт Клиента не найден'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            account.amount += int(amount)
            account.save()
        except ValueError:
            return Response({'error': 'Транзакция не удалась'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'success': 'Транзакция прошла успешно'}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['get'])
    def search_individual_client(self, request):
        query = request.GET.get('query')
        if query:
            clients = self.filter_queryset(self.get_queryset()).filter(
                Q(individual_client__full_name__icontains=query) 
            ).distinct()
        else:
            clients = self.filter_queryset(self.get_queryset())
        
        page = self.paginate_queryset(clients)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(clients, many=True)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def search_company_client(self, request):
        query = request.GET.get('query')
        if query:
            clients = self.filter_queryset(self.get_queryset()).filter(
                Q(company_owners__short_name__icontains=query) |
                Q(company_owners__full_name__icontains=query)
            ).annotate(num_owners=Count('company_owners')).filter(num_owners__gt=0).distinct()
        else:
            clients = self.filter_queryset(self.get_queryset()).annotate(num_owners=Count('company_owners')).filter(num_owners__gt=0)
        
        page = self.paginate_queryset(clients)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(clients, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'search_company_client', 'search_individual_client']:
            return ClientRetrieveSerializer
        if self.action == 'add_balance_to_account':
            return ClientAddBalanceToAccountSerializer
        return self.serializer_class
    
    @action(detail=False, methods=['get'])
    def get_last_num_reg(self, request):
        last_client = Client.objects.last()
        if last_client:
            value = last_client.id
        else: value = 0

        return Response({'last_num_reg': value})

class CompanyViewSet(viewsets.ModelViewSet):
    """Юр лица"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CompanyRetrieveSerializer
        return self.serializer_class

class AccountFilter(FilterSet):
    id = CharFilter()
    acc_num = CharFilter()
    class Meta:
        model = Account
        fields = ['id', 'acc_num']

class AccountViewSet(viewsets.ModelViewSet):
    """Счета"""
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    # search_fields = ['=acc_num', 'id']
    filterset_class = AccountFilter
    ordering_fields = ['id', 'amount', 'date_open']

    @action(detail=False, methods=['get'])
    def excel_list(self, request, *args, **kwargs):
        # Выполняем поиск и фильтрацию
        queryset = self.filter_queryset(self.get_queryset())

        # Ваш сериализатор для преобразования QuerySet в данные Excel
        serializer = self.get_serializer(queryset, many=True)

        # Преобразуем данные сериализатора в список списков (для Excel)
        data = [list(item.values()) for item in serializer.data]

        # Заголовки столбцов
        headers = list(serializer.data[0].keys()) if serializer.data else []

        # Создаем файл Excel
        response = ExcelResponse(data, output_name='account_data', headers=headers, sheet_name='Accounts')

        # response = ExcelResponse(serializer.data, output_name='account_data', sheet_name='Accounts')
        return response


class DocsViewSet(viewsets.ModelViewSet):
    """Документы"""
    queryset = Docs.objects.all()
    serializer_class = DocsSerializer
    permission_classes = [AllowAny]

class ContactViewSet(viewsets.ModelViewSet):
    """Контакты"""
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return ContactRetrieveSerializer
        return self.serializer_class

