from django.shortcuts import get_object_or_404, render
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.all()
    # order_by('-date), shows the latest entry
    # [:5], shows only 5 entries 
    return render (request, 'blogs/all_blogs.html', { 'blogs':blogs })

def detail(request, blog_id):
    # This will try and get an object and if it can't find it then throw a 404
    blog = get_object_or_404(Blog, pk=blog_id)
    return render (request, 'blogs/detail.html', {'id':blog_id})