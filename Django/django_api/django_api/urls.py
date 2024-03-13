from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('cities.urls')),
    path('api/', include('users.urls')),
    path('api/', include('reservations.urls')),
    path('api/', include('incidents.urls')),
]
