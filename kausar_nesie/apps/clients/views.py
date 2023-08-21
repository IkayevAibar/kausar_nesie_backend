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

# class ClientFilter(FilterSet):
#     individual_client__rnn = CharFilter()
#     individual_client__iin = CharFilter()
#     individual_client__full_name = CharFilter()
#     class Meta:
#         model = Client
#         fields = ['individual_client__rnn','individual_client__iin', 'individual_client__full_name', 'individual_client__gender', 'individual_client__is_resident', 'individual_client__country', \
#     'individual_client__client_category']


class ClientViewSet(viewsets.ModelViewSet):
    """Клиент"""
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['is_individual']  # Добавляем поле фильтрации для отбора по типу клиента
    search_fields = ['individualclient__full_name', 'company__full_name']  # Поля, по которым будет выполняться поиск
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

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve', 'search_company_client', 'search_individual_client']:
            return ClientRetrieveSerializer
        if self.action == 'add_balance_to_account':
            return ClientAddBalanceToAccountSerializer
        return self.serializer_class
    
    @action(detail=False, methods=['get'])
    def get_last_num_reg(self, request):
        last_client = Client.objects.order_by('-id').first()  # Получаем последнего клиента по id
        if last_client:
            last_num_reg = last_client.reg_num
            last_num_int = int(last_num_reg)  # Предполагаем, что reg_number является числом
        else:
            last_num_int = 0

        while True:
            new_num_int = last_num_int + 1
            new_num_reg = str(new_num_int).zfill(4)  # Преобразуем в строку, заполняя нулями до 6 символов

            try:
                # Проверяем, нет ли в базе данных клиента с таким номером
                Client.objects.get(reg_num=new_num_reg)
            except Client.DoesNotExist:
                # Если клиент с таким номером не найден, значит, это уникальный номер
                break
            else:
                # Если клиент с таким номером найден, генерируем новый номер и повторяем проверку
                last_num_int = new_num_int

        return Response({'last_num_reg': new_num_reg})

class CompanyViewSet(viewsets.ModelViewSet):
    """Юр лица"""
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return CompanyRetrieveSerializer
        if self.action == 'add_owner_to_company':
            return ClientAddOwnerToCompanySerializer
        return self.serializer_class
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # Instead of returning the full serialized data, return only the 'id' field
        return Response({'company_id': serializer.instance.id}, status=status.HTTP_201_CREATED)


    @action(detail=False, methods=['get'])
    def get_last_num_reg(self, request):
        last_object = Company.objects.order_by('-id').first()  # Получаем последнего клиента по id
        if last_object:
            last_num_reg = last_object.reg_num
            try:
                last_num_int = int(last_num_reg)  # Предполагаем, что reg_number является числом
            except ValueError:
                last_num_int = 0
        else:
            last_num_int = 0

        while True:
            new_num_int = last_num_int + 1
            new_num_reg = str(new_num_int).zfill(6)  # Преобразуем в строку, заполняя нулями до 6 символов

            try:
                # Проверяем, нет ли в базе данных клиента с таким номером
                Company.objects.get(reg_num=new_num_reg)
            except Company.DoesNotExist:
                # Если клиент с таким номером не найден, значит, это уникальный номер
                break
            else:
                # Если клиент с таким номером найден, генерируем новый номер и повторяем проверку
                last_num_int = new_num_int

        return Response({'last_num_reg': new_num_reg})
    
    @action(detail=True, methods=['post'])
    def add_owner_to_company(self, request, pk=None):
        company = self.get_object()

        try:
            owner_id = request.data['owner_id']
        except KeyError:
            return Response({'error': 'owner_id не указан'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            share = request.data['share']
        except KeyError:
            return Response({'error': 'share не указан'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            owner = IndividualClient.objects.get(id=owner_id)
        except IndividualClient.DoesNotExist:
            return Response({'error': 'Владелец не найден'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            CompanyOwner.objects.create(company=company, owner=owner, share=share)
        except:
            return Response({'error': 'Владелец уже добавлен'}, status=status.HTTP_400_BAD_REQUEST)


        return Response({'success': 'Владелец добавлен'}, status=status.HTTP_200_OK)


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

    def create(self, request, *args, **kwargs):
        contacts_data = request.data
        if isinstance(contacts_data, list):
            serializer = self.get_serializer(data=contacts_data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return super().create(request, *args, **kwargs)