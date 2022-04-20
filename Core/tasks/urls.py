from django.urls import path
from . import views

urlpatterns = [
    path('', views.ApiOverview, name='home'),
    path('create/', views.add_tasks, name='add-tasks'),
    path('all/', views.view_tasks, name='view_tasks'),
    path('update/<int:pk>', views.update_Tasks),
    path('delete/<int:pk>', views.delete_task),
]