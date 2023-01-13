from django.shortcuts import render

def hello_world(request, *args, **kwargs):
    return render(request, 'posts/hello_world.html')
