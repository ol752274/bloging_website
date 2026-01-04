from django.shortcuts import render
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
from django.db.models import Q
from blogs.models import Blog
from blogs.models import Category
# Create your views here.
def posts_by_category(request, category_id):
    #Fetch the posts based on category_id
    posts = Blog.objects.filter(status="Published", category=category_id)
    try:
        category = Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context = {
        'posts':posts,
        'category' : category,
    }
    return render(request, 'posts_by_category.html', context)

def blogs(request, slug):
    single_blog = get_object_or_404(Blog,slug=slug,status="Published")
    context = {
        'single_blog': single_blog,
    } 
    return render(request, 'blogs.html',context)
def search(request):
    keyword = request.GET.get('Keyword')
    print('keyword:', keyword)
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(content__icontains=keyword) | Q(blog_body__icontains=keyword), status="Published")
    print(blogs)
    context = {
        'blogs': blogs,
        'keyword': keyword,
    }   
    return render(request, 'search.html', context)