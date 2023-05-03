from .views import *
from rest_framework.routers import DefaultRouter

app_name = "collaterals"

router = DefaultRouter()

router.register(r'collateral', CollateralViewSet)
router.register(r'collateral-insurance', CollateralInsuranceViewSet)
router.register(r'collateral-coclient', CollateralCoclientViewSet)
router.register(r'collateral-assesment', CollateralAssesmentViewSet)


urlpatterns = router.urls