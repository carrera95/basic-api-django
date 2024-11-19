from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from documents.views import DocumentViewSet
from rest_framework import routers
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'documents', DocumentViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/login', views.login),
    path('api/register', views.register),
    path('api/', include('tasks.urls')),
    path('api/', include(router.urls))
]

if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)