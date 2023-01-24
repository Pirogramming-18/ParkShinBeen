from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def main(request):
    posts = Post.objects.all()
    comments_lists = []
    for post in posts:
        comments_lists.append(Comment.objects.filter(post_id = post.id))
    post_and_comment = zip(posts, comments_lists)
    context = {
        'post_and_comment': post_and_comment,
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

@csrf_exempt
def comment_ajax(request):
    req = json.loads(request.body)
    post_id = req['id']
    content = req['content']
    comment = Comment.objects.create(
        post_id = Post.objects.get(id=post_id),
        content = content
    )
    return JsonResponse({'post_id': post_id, 'comment_id': comment.id, 'content': comment.content})

@csrf_exempt
def delete_ajax(request):
    req = json.loads(request.body)
    post_id = req['post_id']
    comment_id = req['comment_id']
    comment = Comment.objects.get(id=comment_id)
    comment.delete()
    return JsonResponse({'post_id': post_id, 'comment_id': comment_id})