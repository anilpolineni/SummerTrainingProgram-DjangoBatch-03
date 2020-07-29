from django.shortcuts import render,redirect
from .forms import UserForm
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout,get_user
#from django.contrib.auth import set_password

from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User

from django.contrib import messages

# Create your views here.

def home(req):
	return render(req,'home.html')


def signup(req):
	form = UserForm()
	if req.method=='POST':
		form = UserForm(req.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("Done")
	return render(req,'register.html',{'form':form})

def signin(req):
	if req.method=='POST':
		username = req.POST['username']
		password = req.POST['password']
		user = authenticate(username=username,password=password)
		if user is not None:
			login(req,user)
		return redirect('signin')

	return render(req,'login.html')
	
@login_required
def signout(req):
	logout(req)
	return redirect('home')

@login_required
def profile(req):
	user = get_user(req)

	return render(req,'profile.html',{"user":user})

@login_required
def changepassword(req):
	user = get_user(req)
	if req.method=='POST':
		if req.POST['new_password'] == req.POST['con-password']:
			user.set_password(req.POST['new_password'])
			user.save()
			return redirect("home")
		return HttpResponse("not match")
	return render(req,"changepassword.html",{'user':user})


def showusers(req):
	data=User.objects.all()
	context={'data':data}
	return render(req,'showusers.html',context)


def edituser(req,id):
	user=User.objects.get(id=id)
	if req.method=="POST":
		first_name=req.POST['first_name']
		last_name=req.POST['last_name']
		username=req.POST['username']
		email=req.POST['email']
		user.first_name=first_name
		user.last_name=last_name
		user.username=username
		user.email=email
		user.save()
		messages.info(req,'%s is successfully updated'%(username))
		return redirect('showusers')
	return render(req,'edituser.html',{'user':user})


def deleteuser(req,id):
	user=User.objects.get(id=id)
	if  req.method=="POST":
		user.delete()
		messages.error(req,'successfully deleted')
		return redirect('showusers')
	return render(req,'deleteuser.html',{'user':user})

