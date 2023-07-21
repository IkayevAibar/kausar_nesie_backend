from .views import *
from rest_framework.routers import DefaultRouter

app_name = "credits"

router = DefaultRouter()

router.register(r'credit', CreditViewSet)
router.register(r'credit-treatments', CreditTreatmentViewSet)
router.register(r'credit-payment-schedule', CreditPaymentScheduleViewSet)
router.register(r'credit-line', CreditLineViewSet)
router.register(r'requisite', RequisiteViewSet)

urlpatterns = router.urls
