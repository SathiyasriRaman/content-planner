from django.shortcuts import render, redirect, get_object_or_404
from .models import Idea

# HOME
def home(request):
    return render(request, "ideas/home.html")

# LIST
def list_ideas(request):
    ideas = Idea.objects.all().order_by('-created_at')
    return render(request, "ideas/list.html", {"ideas": ideas})

# CREATE
def create_idea(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description", "")
        scheduled_date = request.POST.get("scheduled_date") or None

        if title:
            Idea.objects.create(
                title=title,
                description=description,
                scheduled_date=scheduled_date
            )
            return redirect('/ideas/')

    return render(request, "ideas/create.html")


# UPDATE
def update_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)

    if request.method == "POST":
        idea.title = request.POST.get("title")
        idea.description = request.POST.get("description")
        idea.status = request.POST.get("status")
        idea.scheduled_date = request.POST.get("scheduled_date") or None
        idea.save()

        return redirect('/ideas/')

    return render(request, "ideas/update.html", {"idea": idea})


# DELETE
def delete_idea(request, pk):
    idea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        idea.delete()
        return redirect('/ideas/')
    return render(request, "ideas/delete.html", {"idea": idea})
