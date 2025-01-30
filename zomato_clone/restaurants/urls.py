from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='restaurant_index'),
    path('restaurant/<int:restaurant_id>/', views.restaurant_detail, name='restaurant_detail'),
    path('restaurant/<int:restaurant_id>/menu/', views.menu, name='restaurant_menu'),
    path('restaurant/<int:restaurant_id>/order/', views.order, name='restaurant_order'),
]