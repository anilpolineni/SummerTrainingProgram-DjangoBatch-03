from django.shortcuts import render

# Create your views here.
def index(req):
	return render(req,'Action/index.html')
def home(req):
	
	return render(req,'Action/home.html')
def about(req):
	return render(req,"Action/about.html")