from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('faculty/', views.faculty_list, name='faculty_list'),
    path('faculty/<int:pk>/', views.faculty_detail, name='faculty_detail'),
    path('faculty/create/', views.faculty_create, name='faculty_create'),
    path('faculty/<int:pk>/edit/', views.faculty_edit, name='faculty_edit'),
    path('faculty/delete/<int:pk>/', views.faculty_delete, name='faculty_delete'),
    path('faculty/search/', views.faculty_search, name='faculty_search'),
    path('alumni/', views.alumni_list, name='alumni_list'),
    path('alumni/<int:pk>/', views.alumni_detail, name='alumni_detail'),
    path('alumni/create/', views.alumni_create, name='alumni_create'),
    path('alumni/search/', views.alumni_search, name='alumni_search'),
    path('alumni/<int:pk>/edit/', views.alumni_edit, name='alumni_edit'),
    path('alumni/delete/<int:pk>/', views.alumni_delete, name='alumni_delete'),
]