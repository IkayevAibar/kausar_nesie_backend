from .views import *
from rest_framework.routers import DefaultRouter

app_name = "clients"

router = DefaultRouter()

router.register(r'individual_client', IndividualClientViewSet)
router.register(r'address', AddressViewSet)
router.register(r'id-card', IdCardViewSet)
router.register(r'account', AccountViewSet)
router.register(r'company', CompanyViewSet)
router.register(r'client', ClientViewSet)


urlpatterns = router.urls