from django.shortcuts import render
from djangocrudmongodbapp.models import Posts
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

@csrf_exempt
def add_post(request):
    comment = request.POST.get("comment").split(",")
    tags = request.POST.get("tags").split(",")
    user_details = {'first_name':request.POST.get("first_name"),'last_name':request.POST.get("last_name")}
    post = Posts(post_title=request.POST.get("post_title"),post_description=request.POST.get("post_description"),
                comment=comment,tags=tags,user_details=user_details)
    post.save()
    return HttpResponse("inserted")
@csrf_exempt
def update_post(request,id):
    post = Posts.objects.get(id=id)
    post.user_details["first_name"] = request.POST.get("first_name")
    post.save()
    return HttpResponse("updated")

@csrf_exempt
def delete_post(request,id):
     post = Posts.objects.get(id=id)
     post.delete()
     return HttpResponse("post deleted")

def read_post(request,id):
    post = Posts.objects.get(id=id)
    value="First name : "+post.user_details["first_name"]+"\n last_name : "+post.user_details["last_name"]+ "\n post title : "+post.post_title+"\n post description : "+post.post_description
    allcomment=""
    for comment in post.comment:
        allcomment+=comment+","
    value += "\n comments : "+allcomment
    return HttpResponse(value)

def read_post_all(request):
    posts = Posts.objects.all()
    value=""
    for post in posts:
        value+="First name : "+post.user_details["first_name"]+"\n last_name : "+post.user_details["last_name"]+ "\n post title : "+post.post_title+"\n post description : "+post.post_description
        allcomment=""
        for comment in post.comment:
            allcomment+=comment+","
        value += "\n comments : "+allcomment
    return HttpResponse(value)
    





