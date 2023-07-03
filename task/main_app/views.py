from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Project
from accounts.models import Profile, Uchat
from django.views.generic.edit import CreateView, UpdateView

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


class ChatView(CreateView):
    model = Uchat
    template_name = 'chat.html'
    fields = ["message"]
    success_url = "/chat/"

    def form_valid(self, form):
        form.instance.sender = self.request.user
        return super().form_valid(form)
