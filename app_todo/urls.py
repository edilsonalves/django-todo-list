from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('delete/<int:todo_id>/', views.delete),
]
