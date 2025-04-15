# pedido_app/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # API (uso de DRF)
    path('api/', include('recetas.api_urls', namespace='recetas_api')),

    # Web de recetas (HTML)
    path('recetas/', include('recetas.web_urls', namespace='recetas')),  # 👈 SOLO web_urls.py acá

    # Login/Logout de Django
    path('accounts/', include('django.contrib.auth.urls')),

    # Token JWT para API
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# Para servir archivos MEDIA en desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
