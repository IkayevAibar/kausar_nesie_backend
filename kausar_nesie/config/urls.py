from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls
from apps.catalog.urls import router as catalog_router
from apps.clients.urls import router as clients_router
from apps.collaterals.urls import router as collaterals_router
from apps.credits.urls import router as credits_router

router = routers.DefaultRouter()

router.registry.extend(catalog_router.registry)
router.registry.extend(clients_router.registry)
router.registry.extend(collaterals_router.registry)
router.registry.extend(credits_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='API docs')),
]

urlpatterns += [
    path('api/auth/', include('Oauth.urls', namespace='Oauth')),
    path('api/clients/', include('apps.clients.urls', namespace='clients')),
    path('api/catalog/', include('apps.catalog.urls', namespace='catalog')),
    path('api/collaterals/', include('apps.collaterals.urls', namespace='collaterals')),
    path('api/credits/', include('apps.credits.urls', namespace='credits')),
    # path('api/', include(router.urls))
]
