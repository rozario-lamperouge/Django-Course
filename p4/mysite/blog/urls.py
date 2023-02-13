from django.contrib import admin
from django.urls import path
from blog.views import PostList

urlpatterns =[
	path('',PostList.as_view()),
]