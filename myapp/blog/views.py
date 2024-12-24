from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello world, You are at the blog index") #args

# more urls and views

def details(request):
    return HttpResponse("You viewing post details page")

#dynamic urls

def dynamic(request, post_id):
    return HttpResponse(f"You are visibling the dynaic urls section where in the urls the number are visisble and the id : {post_id}")


# REDIRECTING

def old_url_redirect(request):
    return redirect("new_url")

def new_url_view(request):
    return HttpResponse("This the redurection page : new_url_view")
