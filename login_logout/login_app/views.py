from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login_app/login/')
def home_view(request):
    return render(request, "login_app/home.html")

