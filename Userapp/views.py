from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View

from .models import Account


class Loginview(View):
    def get(self,request):
        return render(request, "page-user-login.html")

    def post(self,request):
        log = request.POST.get('l')
        par = request.POST.get('p')
        userlar = authenticate( request, username=log,password=par)
        if userlar is None:
            return redirect("login")
        login(request, userlar)
        return redirect("home")

class Regview(View):
    def get(self,request):
        return render(request, "page-user-register.html")

    def post(self, request):
        p1 = request.POST.get("p1")
        p2 = request.POST.get("p2")
        e = request.POST.post("e")
        p = request.POST.post("p1")
        if p1==p2:
            user = User.objects.create_superuser(
                    username=e,
                    password=p
            )
        else:
            return redirect("register")
        Account.objects.create(
            ism = request.POST.post("i"),
            familya = request.POST.post("f"),
            email = request.POST.post("e"),
            mamlakat = request.POST.post("m"),
            shahar = request.POST.post("sh"),
            user = user
        )
        return redirect("home")

