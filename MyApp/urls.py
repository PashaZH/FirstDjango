from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('items/', views.item_list, name='item_list'),
]