from django.shortcuts import render
from django.views.generic import ListView
from blog.models import post

# Create your views here.
class PostList(ListView):
	queryset = post.objects.order_by("-date")
	template_name = "blog/list.html"

def postdetail(request, id):
	p = post.objects.get(id=id)
	return render(request, "blog/postdetail.html", {'p':p})