from django.urls import path
from Action import views
urlpatterns=[
	path('index/',views.index,name="index"),
	path('home/',views.home,name="home"),
	path('about/',views.about,name='about'),


]