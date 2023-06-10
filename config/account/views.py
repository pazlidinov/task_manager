from django.shortcuts import render
from .forms import ProfileUserCreationForm
# Create your views here.

def home(request):
    return render(request, 'auth/profile.html')

def register(request):
    form = ProfileUserCreationForm()
    if request.method == 'POST':
        form = ProfileUserCreationForm(request.POST)
        if form.is_valid():
            u = form.save()
            authenticate(u)
            login(request, u)
            return redirect("/")
        else:
            # message = "Incorrect username or password!"
            # messages.add_message(request, messages.ERROR, message)
            return render(request, "account/register.html", {"form": form})
    return render(request, "account/register.html", {"form": form})