from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
	# return HttpResponse("<h1>Hello Everyone, I'm Richard and this is my website!</h1>")
	return render(request, 'main/home.html')