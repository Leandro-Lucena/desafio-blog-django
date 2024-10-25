from django.shortcuts import render
from .models import Post, Tag

# Create your views here.

def blog_view(request):
    posts = Post.objects.all()
    tags = Tag.objects.all()
    return render(request, 'admin/core/blog.html', {'posts': posts, 'tags': tags})