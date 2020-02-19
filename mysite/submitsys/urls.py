from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('assignments', views.assignment_console, name='assignment_console'),
    path('assignments/create', views.assignment_create, name='assignment_create'),
    path('<int:assignment_id>/', views.detail, name='detail'),
    path('<int:assignment_id>/student/', views.student, name='student'),
]