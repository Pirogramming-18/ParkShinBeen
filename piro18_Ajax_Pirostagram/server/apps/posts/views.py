from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    posts = Post.objects.all()
    context = {
        'posts': posts,
    }
    return render(request, 'posts/main.html', context=context)

def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:main')
        else:
            ctx = {
                'form': form,
            }
            return render(request, 'posts/post_new.html', ctx)
    elif request.method == 'GET':
        form = PostForm()
        ctx = {
            'form': form,
        }
        return render(request, 'posts/post_new.html', ctx)

def delete(request, pk):
    if request.method == "POST":
        post = Post.objects.get(id=pk)
        post.delete()
    return redirect('posts:main')

@csrf_exempt
def like_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    button_type = req['type']
    post = Post.objects.get(id=post_id)
    if button_type == 'like':
        post.like += 1
        post.pressed = True
        post.save()
        return JsonResponse({'id': post_id, 'type': button_type, 'num': post.like})
    else:
        post.like -= 1
        post.pressed = False
        post.save()
        return JsonResponse({'id': post_id, 'type': button_type, 'num': post.like})