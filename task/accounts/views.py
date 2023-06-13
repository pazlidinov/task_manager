from .forms import LoginForm, RegistrationForm, ProfileUpdateForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View, UpdateView
from .models import Profile
from django.urls import reverse_lazy
# Create your views here.


class ProfilePage(LoginRequiredMixin, View):
    template_name = 'auth/profile.html'

    def get(self, request):
        if request.user.is_authenticated:
            return render(request, self.template_name, {"object": request.user})
        else:
            return redirect('accounts:login')


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        user = authenticate(
            username=form.data['username'], password=form.data['password'])
        if user is not None:
            login(request, user)
            return redirect("accounts:profile")
        else:
            print("ERROR")
            return render(request, 'auth/login.html', {"form": form})

    form = LoginForm()
    return render(request, 'auth/login.html', {"form": form})


def logout_page(request):
    logout(request)
    return redirect("/accounts/login/")


def registration_page(request):

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            u = form.save(commit=False)
            full_name = request.POST.get('full_name').strip().split(' ')
            if full_name is not None:
                u.first_name = full_name[0]
                u.last_name = full_name[1]
            u.save()
            authenticate(u)
            login(request, u)
            return redirect("accounts:profile")
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'auth/registration.html', context)


class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileUpdateForm
    template_name = 'auth/profile_edit.html'
    success_url = reverse_lazy("accounts:profile")

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)

        context.update({
            'object': self.get_object,
        })
        return context
