from .views import *
from rest_framework.routers import DefaultRouter

app_name = "credits"

router = DefaultRouter()

router.register(r'credit', CreditViewSet)

urlpatterns = router.urls
