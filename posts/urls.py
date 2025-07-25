"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from .views import *
urlpatterns = [
    path('', home , name='home'),
    path('category/<slug:tag>', home, name='category_view'),
    path('post_create/', post_create_view , name='post_create'),
    path('post_delete/<uuid:pk>', post_delete_view, name='post_delete'),
    path('post_edit/<uuid:pk>', post_edit_view, name='post_edit'),
    path('post_read/<uuid:pk>', post_read_view, name='post_read'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


