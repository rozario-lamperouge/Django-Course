from django.contrib import admin
from django.urls import path
from blog.views import PostList
from . import views

urlpatterns =[
	path('',PostList.as_view()),
	path('<int:id>',views.postdetail, name="postdetail")
]