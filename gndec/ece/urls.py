"""
URL configuration for gndec project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views
from .views import (
    StudentListView, 
    StudentDetailView, 
    StudentCreateView, 
    StudentUpdateView, 
    StudentDeleteView
)

urlpatterns = [
    path("home/", views.home, name = "home"),
    path("products/", views.products, name = "products"),
    path("service/", views.service, name = "service"),
    path("contacts/", views.contacts, name = "contacts"),
    
    path('students/', StudentListView.as_view(), name='student-list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    path('students/new/', StudentCreateView.as_view(), name='student-create'),
    path('students/<int:pk>/edit/', StudentUpdateView.as_view(), name='student-update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student-delete'),

]
