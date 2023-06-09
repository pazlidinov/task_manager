from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "auth/profile.html"
    

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context["user"] = User.objects.get()
    #     return context


def my_login(request):
    if request.method == 'POST':
        phone_number = request.POST.get("phone_number")
        password = request.POST.get("password")

        user = User.objects.get(phone_number=phone_number, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            print("OK")
            return redirect('/')
        else:
            # No backend authenticated the credentials
            print("error")
            return render(request, "auth/login.html")
    return render(request, "auth/login.html")


def logged_out(request):
    logout(request)
    return redirect("/accounts/login/")
