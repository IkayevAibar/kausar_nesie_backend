from django.urls import path
from .views import *

app_name = "clients"

urlpatterns = [
    path('individual_client/', IndividualClientView.as_view()),
    path('adress/', AddressView.as_view()),
    path('id-card/', IdCardView.as_view()),
    path('account/', AccountView.as_view()),
    path('company/', CompanyView.as_view()),
    path('сlient/', ClientView.as_view()),

]