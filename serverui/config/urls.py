from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('monitoring/', include('apps.monitoring.urls')),
    #path('control/', include('apps.control.urls')),
]
