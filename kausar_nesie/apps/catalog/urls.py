from django.urls import path
from .views import *
from rest_framework.routers import DefaultRouter

app_name = "catalog"

router = DefaultRouter()
router.register(r'address_type', AddressTypeViewSet)
router.register(r'contact', ContactViewSet)
router.register(r'areas', AreasViewSet)
router.register(r'cities', CitiesViewSet)
router.register(r'client_category', ClientCategoryViewSet)
router.register(r'category_type', CategoryTypeViewSet)
router.register(r'work_type', WorkTypeViewSet)
router.register(r'transaction_type', TransactionTypeViewSet)
router.register(r'status', StatusViewSet)
router.register(r'sector_econ', SectorEconViewSet)
router.register(r'project_type', ProjectTypeViewSet)
router.register(r'position_type', PositionTypeViewSet)
router.register(r'period_type', PeriodTypeViewSet)
router.register(r'payment_type', PaymentTypeViewSet)
router.register(r'org_form', OrgFormViewSet)
router.register(r'link_type', LinkTypeViewSet)
router.register(r'line_type', LineTypeViewSet)
router.register(r'idcard_type', IdCardViewSet)
router.register(r'form_property', FormPropertyViewSet)
router.register(r'currencies', CurrenciesViewSet)
router.register(r'credit_target', CreditTargetViewSet)
router.register(r'credit_source', CreditSourceViewSet)
router.register(r'country', CountryViewSet)
router.register(r'counters', CountersViewSet)
router.register(r'contact_type', ContactTypeViewSet)
router.register(r'collateral_type', CollateralTypeViewSet)
router.register(r'dept_type', DeptTypeViewSet)
router.register(r'bank', BankViewSet)
router.register(r'calculate', CalculateViewSet)
router.register(r'base_account', BaseAccountViewSet)

urlpatterns = router.urls