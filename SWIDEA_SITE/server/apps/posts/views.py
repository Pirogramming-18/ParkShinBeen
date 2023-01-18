from django.shortcuts import render, redirect
from server.apps.posts.models import *

def tool_create(request, *args, **kwargs):
    if request.method == "POST":
        tool = Tool.objects.create(
            name = request.POST['name'],
            kind = request.POST['kind'],
            content = request.POST['content'],
        )
        return redirect(f'/tool/{tool.id}')
    return render(request, 'idea/tool_create.html')

def tool_list(request, *args, **kwargs):
    tools = Tool.objects.all()
    context = {
        "tools": tools,
    }
    return render(request, 'idea/tool_list.html', context=context)

def tool_detail(request, pk, *args, **kwargs):
    tool = Tool.objects.all().get(id=pk)
    idea_possible = Idea.objects.filter(devtool=tool)
    context = {
        "tool": tool,
        "ideas": idea_possible,
    }
    return render(request, "idea/tool_detail.html", context=context)

def tool_update(request, pk, *args, **kwargs):
    tool = Tool.objects.get(id=pk)
    if request.method == "POST":
        tool.name = request.POST['name']
        tool.kind = request.POST['kind']
        tool.content = request.POST['content']
        tool.save()
        return redirect(f"/tool/{tool.id}")
    context={
        "tool": tool
    }
    return render(request, "idea/tool_update.html", context=context)

def tool_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        tool = Tool.objects.get(id=pk)
        tool.delete()
    return redirect("/tool/list")

def idea_list(request, *args, **kwargs):
    ideas = Idea.objects.all()
    devtools = []
    for idea in ideas:
        devtools.append(Tool.objects.get(id=idea.devtool.id))
    ideas_and_devtool = zip(ideas, devtools)
    context = {
        "ideas_and_devtool": ideas_and_devtool
    }
    return render(request, 'idea/idea_list.html', context=context)

def idea_create(request, *args, **kwargs):
    if request.method == "POST":
        idea = Idea.objects.create(
            title=request.POST["title"],
            image=request.FILES.get("image"),
            content=request.POST["content"],
            interest=request.POST["interest"],
            devtool=Tool.objects.get(id=request.POST["devtool"]),
        )
        return redirect(f"/idea/{idea.id}")
    tools = Tool.objects.all()
    context = {
        "tools": tools,
    }
    return render(request, "idea/idea_create.html", context=context)

def idea_detail(request, pk, *args, **kwargs):
    idea = Idea.objects.all().get(id=pk)
    context = {
        "idea": idea,
    }
    return render(request, "idea/idea_detail.html", context=context)

def idea_update(request, pk, *args, **kwargs):
    idea = Idea.objects.get(id=pk)
    if request.method == "POST":
        idea.title=request.POST["title"]
        idea.image=request.FILES.get("image")
        idea.content=request.POST["content"]
        idea.interest=request.POST["interest"]
        idea.devtool=Tool.objects.get(id=request.POST["devtool"])
        idea.save()
        return redirect(f"/idea/{idea.id}")
    tools = Tool.objects.all()
    context={
        "idea": idea,
        "tools": tools,
    }
    return render(request, "idea/idea_update.html", context=context)

def idea_delete(request, pk, *args, **kwargs):
    if request.method == "POST":
        idea = Idea.objects.get(id=pk)
        idea.delete()
    return redirect("/")