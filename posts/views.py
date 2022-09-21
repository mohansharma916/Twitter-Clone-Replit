from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.

def index(request):
    #if the method is Post
    if request.method=='POST':
        form =PostForm(request.POST, request.FILES)
            #if the form is valid
        if form.is_valid():
                #yes Save
            form.save()
                #redirect to home
            return HttpResponseRedirect('/') 
        else:
            return HttpResponseRedirect(form.errors.as_json())

            
    # get all the posts limit =20
    posts=Post.objects.all()[:20]

    #show all the posts
    return render(request,'posts.html',

                        {'posts':posts})

def delete(request,post_id):
    #find user 
    post=Post.objects.get(id=post_id)
    post.delete() 
    output="Post Id is "+ str(post_id)
    return HttpResponseRedirect("/")

def edit(request,post_id):
    post=Post.objects.get(id=post_id)
    if request.method=="GET":
        return render(request,"edit.html",{"post":post})
    if request.method=="POST":
        editposts=Post.objects.get(id=post_id)
        form=PostForm(request.POST,request.FILES,instance=editposts)
        if form.is_valid():

                #yes Save
            form.save()
                #redirect to home
            return HttpResponseRedirect('/') 
        else:
            return HttpResponse("not Valid")

def like(request,post_id):
    count=Post.objects.get(id=post_id)
    if count.count==0:
        count.count += 1
        count.save()
    elif count.count==1:
        count.count-=1
        count.save()
    return HttpResponseRedirect("/")