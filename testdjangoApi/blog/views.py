from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog_list(request):
    querysets = Blog.objects.all()
    return render(request, 'blog_list.html', {'qs':querysets})

def blog_detail(request,**kwargs):
    pk = kwargs['pk']
    blog = Blog.objects.get(pk=pk)
    return render(request, 'blog_detail.html',{'blog':blog})



