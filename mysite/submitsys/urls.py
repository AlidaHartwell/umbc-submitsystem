from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:assignment_id>/', views.detail, name='detail'),
    path('<int:assignment_id>/student/', views.student, name='student'),
]