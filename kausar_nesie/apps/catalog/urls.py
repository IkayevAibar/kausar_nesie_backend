from django.urls import path
from .views import *

app_name = "catalog"

urlpatterns = [
    path('adress_type/', AddressTypeView.as_view()),
    path('contact/', ContactView.as_view()),
    path('areas/', AreasView.as_view()),
    path('citites/', CitiesView.as_view()),
    path('client_category/', ClientCategoryView.as_view()),
    path('category_type/', CategoryTypeView.as_view()),
    path('work_type/', WorkTypeView.as_view()),
    path('transaction_type/', TransactionTypeView.as_view()),
    path('status/', StatusView.as_view()),
    path('sector_econ/', SectorEconView.as_view()),
    path('project_type/', ProjectTypeView.as_view()),
    path('position_type/', PositionTypeView.as_view()),
    path('period_type/', PeriodTypeView.as_view()),
    path('payment_type/', PaymentTypeView.as_view()),
    path('org_form/', OrgFormView.as_view()),
    path('link_type/', LinkTypeView.as_view()),
    path('line_type/', LineTypeView.as_view()),
    path('idcard_type/', IdcardTypeView.as_view()),
    path('form_property/', FormPropertyView.as_view()),
    path('currencies/', CurrenciesView.as_view()),
    path('credit_target/', CreditTargetView.as_view()),
    path('credit_source/', CreditSourceView.as_view()),
    path('country/', CountryView.as_view()),
    path('counters/', CountersView.as_view()),
    path('contact_type/', ContactTypeView.as_view()),
    path('bank/', BankView.as_view()),
    path('calculate/', CalculateView.as_view()),
    path('base-account/', BaseAccountView.as_view()),

]
