from django.shortcuts import render
from django.shortcuts import redirect
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