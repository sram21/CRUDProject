from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_show, name='home'),
    path('edit/<int:id>/', views.update_data, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete')
]
