from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/<int:course_id>/assignments', views.assignment_console, name='assignment_console'),
    path('courses/<int:course_id>/assignments/create', views.assignment_create, name='assignment_create'),
    path('<int:assignment_id>/', views.detail, name='assignment_details'),
    path('<int:assignment_id>/student/', views.student, name='student'),
]