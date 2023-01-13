from django.shortcuts import render, redirect
from server.apps.posts.models import Post


def posts_list(request, *args, **kwargs):
    posts = Post.objects.all()
    order = request.GET.get("order")
    if order:
        posts = Post.objects.order_by(order)

    hours = [post.running_time // 60 for post in posts]
    mins = [post.running_time % 60 for post in posts]
    posts_and_times = zip(posts, hours, mins)

    order_mode = [("", "등록 순"), ("title", "제목 빠른 순"), ("-title", "제목 느린 순"), ("-rate", "별점 높은 순"), ("rate", "별점 낮은 순"), ("-running_time", "상영 시간 긴 순"), ("running_time", "상영 시간 짧은 순")]
    return render(request, 'posts/posts_list.html', {"posts_and_times": posts_and_times, "order_mode": order_mode, "order": order})

def posts_detail(request, pk, *args, **kwargs):
    post = Post.objects.all().get(id=pk)
    return render(request, "posts/posts_detail.html", {"post": post, "hour": post.running_time // 60, "min": post.running_time % 60})

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
    genre_list = Post.MOVIE_GENRE
    return render(request, 'posts/posts_create.html', {"genre_list": genre_list})

def posts_update(request, pk, *args, **kwargs):
    post = Post.objects.get(id=pk)
    genre_list = Post.MOVIE_GENRE
    if request.method == "POST":
        post.title = request.POST['title']
        post.year = request.POST['year']
        post.director = request.POST['director']
        post.main_actor = request.POST['main_actor']
        post.genre = request.POST['genre']
        post.rate = request.POST['rate']
        post.running_time = request.POST['running_time']
        post.review = request.POST['review']
        post.save()
        return redirect(f"/posts/{post.id}")

    return render(request, "posts/posts_update.html", {"post": post, "genre_list": genre_list})

def posts_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect("/")