from django.shortcuts import render

def idea_list(request, *args, **kwargs):
    return render(request, 'idea/base.html')