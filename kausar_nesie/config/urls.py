from django.contrib import admin
from django.urls import path, include

from rest_framework.documentation import include_docs_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='API docs')),
]

urlpatterns += [
    path('api/clients/', include('apps.clients.urls', namespace='clients')),
    path('api/catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('api/collaterals/', include('apps.collaterals.urls', namespace='collaterals')),
    path('api/credits/', include('apps.credits.urls', namespace='credits')),
    path('api/auth/', include('Oauth.urls', namespace='authentication')),
]

urlpatterns += [
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]