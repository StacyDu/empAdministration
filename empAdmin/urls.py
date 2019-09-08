"""empAdmin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from employers.views import (
    DeveloperCreateView,
    HomeView,
    TechnologyCreateView,
    ShowTechnologiesView,
    ShowDevelopersView,
    DeveloperView,
    DeveloperDeleteView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_developer/', DeveloperCreateView.as_view()),
    path('', HomeView.as_view()),
    path('add_technology/', TechnologyCreateView.as_view(), name='add-technology-view'),
    path('show_technologies/', ShowTechnologiesView.as_view(), name='show-technologies-view'),
    path('show_developers/', ShowDevelopersView.as_view(), name='show-developers-view'),
    path('developer_view/<int:pk>/', DeveloperView.as_view(), name='show-developer'),
    path('delete_developer/<int:pk>/', DeveloperDeleteView.as_view(), name='delete-developer'),
]
