from django.shortcuts import render, get_object_or_404
from .models import Blog

def blog_home(request):
    all_blogs = Blog.objects.all()
    return render(request,'blog/bloghome.html', {'allblogs':all_blogs})

def blog_detail(request,pk):
    blog = get_object_or_404(Blog,pk=pk)
    return render(request,'blog/blogdetail.html', {'blog':blog})
