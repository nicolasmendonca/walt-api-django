from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api/user/', include('user.urls')),
    path('api/company/', include('company.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
