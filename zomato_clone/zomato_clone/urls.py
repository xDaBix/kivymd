from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('restaurants/', include('restaurants.urls')),
    path('users/', include('users.urls')),
    path('orders/', include('orders.urls')),
]