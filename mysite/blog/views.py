#for login requiremnet
from django.contrib.auth.decorators import login_required
#staff member to access
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404, redirect
#to avoid seeing str, int error we r gonna take the help of the below module
from django.http import Http404, HttpResponse,HttpResponseRedirect
# Create your views here.
from .models import Blogpost
from .forms import BlogPostForm, BlogPostModelForm
#from django.utils import timezone

#get-> 1 object
#filter-> [] objects
'''
def blog_post_detail_page(request,slug):
    queryset=Blogpost.objects.filter(slug=slug)
    if queryset.count() >=1:
        obj=queryset.first() 
    
    #obj=get_object_or_404 (Blogpost, slug=slug)
    
    try:
        obj=Blogpost.objects.get(id=id  )#query-> database ->data-> django renders it
    except Blogpost.DoesNotExits:
        raise Http404
    except ValueError:
        raise Http404
    
    template_name='blog_post_detail.html'
    context={"object":obj}
    return render (request, template_name, context)
'''
#CRUD

def blog_post_list_view(request):
    #list out objects
    #search view
    #now=timezone.now()
    qs=Blogpost.objects.all().published() # queryset -> list of python objects
    #qs-Blogpost.objects.filter(publish_date__lte=now)
    if request.user.is_authenticated:
        my_qs=Blogpost.objects.filter(user=request.user)
        qs=(qs | my_qs).distinct()
    template_name='blog/list.html'
    context={"object_list":qs}
    return render (request, template_name, context)

#wrapper   to check whether the user is having a valid session or not
@staff_member_required   
def blog_post_create_view(request):
    #create objects using a form
    form= BlogPostModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj= form.save(commit=False)
        obj.user=request.user
        
        obj.save()
        form= BlogPostModelForm()
        
    
    template_name='form.html'
    context={"form":form}
    return render (request, template_name, context)
    
    
def blog_post_retrieve_view(request,slug):
    #similAR to list
    # 1 object detail view
    obj=get_object_or_404 (Blogpost, slug=slug) 
    #print(obj.title)
    template_name='blog/detail.html'
    context={"object":obj }
    return render (request, template_name, context)

@staff_member_required
def blog_post_update_view(request,slug):
    obj=get_object_or_404 (Blogpost, slug=slug)
    form= BlogPostModelForm(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
    template_name='form.html'
    context={  "title":f"Update {obj.title}",'form':form}
    return render (request, template_name, context)

@staff_member_required
def blog_post_delete_view(request,slug):
    obj=get_object_or_404 (Blogpost, slug=slug)
    template_name='blog/delete.html'
    if request.method== "POST":
        obj.delete()
        return redirect("/blog")
    context={"object":obj}
    return render (request, template_name, context)

def blog_post_like(request,slug):
    obj=get_object_or_404 (Blogpost, slug=slug)
    if request.method=="POST":
        print(obj.title)
        obj.likes+=1
        obj.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    

def blog_post_dislike(request,slug):
    obj=get_object_or_404 (Blogpost, slug=slug)
    if request.method=="POST":
        obj.dislikes+=1
        obj.save()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
