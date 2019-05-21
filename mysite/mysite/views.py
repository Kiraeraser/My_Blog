#from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
from .forms import ContactForm
from blog.models import Blogpost

def home_page(request):
    my_title="Welcome to My Blogs....."
    qs= Blogpost.objects.all()[:5]
    contents={'title':my_title, 'blog_list':qs}

    
    return render(request, "hello.html",contents)

def about_us(request):
    my_title="About....."
    contents={'title':my_title}
    return render(request,"about.html",contents)

def contact_us(request):
    form=ContactForm(request.POST or None)
    if form.is_valid():
        print(form.cleaned_data)
        form=ContactForm()
    contents={'title':"Contact Us","form":form}
    
    return render(request,"form.html",contents)