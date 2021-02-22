from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from .views import *
  
urlpatterns = [ 
    path('image_upload', image_view, name = 'image_upload'), 
    path('search/', SearchPage, name='search_result'),
    path('', image_view, name='clear_search'),
] 
  
