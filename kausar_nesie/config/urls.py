from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += [
    path('api/auth/', include('Oauth.urls', namespace='Oauth')),
    path('api/clients/', include('apps.clients.urls', namespace='clients')),
    path('api/catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('api/collaterals/', include('apps.collaterals.urls', namespace='collaterals')),
    path('api/credits/', include('apps.credits.urls', namespace='credits')),
]
