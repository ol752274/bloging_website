from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from blogs.models import Category
from blogs.models import Blog
from assignments.models import About
from .forms import RegistrationForm
def home(request):
    categories = Category.objects.all()
    featured_posts = Blog.objects.filter(is_featured=True,status="Published").order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False,status="Published")
    try:
        about = About.objects.get()
    except:
        about = None
    context = {
        'categories': categories,
        'featured_posts': featured_posts,
        'posts': posts,
        'about': about,
    }
    return render(request,'home.html', context)
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
        else:
            print(form.errors)
    else:
        form = RegistrationForm()
    context = {
        'form' : form,
    }
    return render(request, 'register.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            # Log the user in
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
            return redirect('dashboard')
        else:
            print(form.errors)
    form  = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')