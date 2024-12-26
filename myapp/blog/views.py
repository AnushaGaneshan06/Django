from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse

# ----global variable-------
post = [
        {"id":1, "title" : "Post 1", "content" : "content of Post 1"},
        {"id":2, "title" : "Post 2", "content" : "content of Post 2"},
        {"id":3, "title" : "Post 3", "content" : "content of Post 3"},
        {"id":4, "title" : "Post 4", "content" : "content of Post 4"},
    ]
# ------------------------


def index(request):
    # ----------interpolation -------
    blog_title = "lastest Post"
    return render(request, "blog/index.html", {"blog_title" : blog_title, "post" : post}) #args


#dynamic urls

def dynamic(request, post_id):
    posts = next((item for item in post if item["id"] == post_id), "None")
    return render(request, "blog/detail.html", {'posts' : posts}) #varibale


# more urls and views

def details(request):
    return HttpResponse("You viewing post details page")


# REDIRECTING

def old_url_redirect(request):
    return redirect("new_url/ ")

def new_url_view(request):
    return HttpResponse("This the redurection page : new_url_view")


# Reverse snd the named urls(this helpd to furtehr change of the urls in future bc we use name )

def reverse_urls(request):
    return redirect(reverse('blog:new_page_url'))

