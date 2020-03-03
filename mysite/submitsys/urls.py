from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('courses', views.course_console, name='course_console'),
    path('courses/create', views.course_create, name='course_create'),
    path('courses/<int:course_id>/assignments', views.assignment_console, name='assignment_console'),
    path('courses/<int:course_id>/assignments/create', views.assignment_create, name='assignment_create'),
    path('<int:assignment_id>/', views.detail, name='detail'),
    path('<int:assignment_id>/student/', views.student, name='student'),
]