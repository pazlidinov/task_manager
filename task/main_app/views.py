from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Project
from accounts.models import Profile

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'task-list.html'


def profile_project_add(request):
    if request.method == 'POST':
        author = Profile.objects.get(id=request.user.id)
        print(author)
        Project.objects.create(
            author=author,
            project_name=request.POST.get('project_name'),
            project_link=request.POST.get('project_link'),
            poster=request.POST.get('poster')
        )
        print('ok')
    return redirect("accounts:profile")
