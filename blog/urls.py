from django.urls import path
from django.contrib.auth import views as authViews
from . import views

 
from .views import (
    BlogListView,
    BlogDetailView,
    
)
 
urlpatterns = [
    path('', BlogListView.as_view(), name='home'),  
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # новое изменение

]