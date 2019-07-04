from django.shortcuts import render

def helloWorld(request):
    return render(request, 'blog_list.html')