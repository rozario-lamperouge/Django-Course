from django.shortcuts import render
from django.views.generic import ListView
from blog.models import post

# Create your views here.
class PostList(ListView):
	queryset = post.objects.order_by('-date')
	template_name = 'blog/blog.html'

def postDetail(request,id):
	nxt = id+1
	prv = id-1
	p = post.objects.get(id=id)
	return render(request, 'blog/post.html', {'post':p,'Next':nxt,'Previous':prv})