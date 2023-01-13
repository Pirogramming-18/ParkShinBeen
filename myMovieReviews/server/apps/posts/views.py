from django.shortcuts import render, redirect
from server.apps.posts.models import Post

def hello_world(request, *args, **kwargs):
    return render(request, 'posts/hello_world.html')


def posts_list(request, *args, **kwargs):
    posts = Post.objects.all()

    return render(request, 'posts/posts_list.html', {"posts": posts})

def posts_detail(request, pk, *args, **kwargs):
    post = Post.objects.all().get(id=pk)
    return render(request, "posts/posts_detail.html", {"post": post})

def posts_create(request, *args, **kwargs):
    if request.method == "POST":
        Post.objects.create(
            title = request.POST['title'],
            year = request.POST['year'],
            director = request.POST['director'],
            main_actor = request.POST['main_actor'],
            genre = request.POST['genre'],
            rate = request.POST['rate'],
            running_time = request.POST['running_time'],
            review = request.POST['review'],
        )
        return redirect("/")
    return render(request, 'posts/posts_create.html')