from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from documents.views import DocumentViewSet
from rest_framework import routers
from . import views
from django.urls import path 
from rest_framework_simplejwt.views import ( 
    TokenObtainPairView, 
    TokenRefreshView, 
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', views.login),
    path('api/register', views.register),
    path('api/', include('tasks.urls')),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)