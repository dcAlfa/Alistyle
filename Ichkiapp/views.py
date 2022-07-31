from django.shortcuts import render, redirect
from django.views import View

from Userapp.models import *

from  .models import *
from Alistyleapp.models import *


class TanlanganView(View):
    def get(self, request):
         return render(request, "page-profile-wishlist.html")

class SavatView(View):
    def get(self, request):
        ac = Account.objects.get(user=request.user)
        savatlar = Savat.objects.filter(account=ac)
        ch = [s.mahsulot.chegirma for s in savatlar]
        n = [s.narx for s in savatlar]
        data = {
            "savatlar": savatlar,
            "umumiy": sum(n) ,
            "chegirma": sum(ch) ,
            "yakuniy": sum(n)-sum(ch)
        }
        return render(request, "page-shopping-cart.html", data )

class SavatQoshView(View):
    def get(self,request, pk):
        m = Mahsulot.objects.get(id=pk)
        savatlar = Savat.objects.filter(mahsulot=m)
        if len(savatlar)==0:
            Savat.objects.create(
                mahsulot = m,
                account = Account.objects.get(user=request.user),
                narx = m.narx
            )
        return  redirect("mahsulot", pk)
def savat_k(request, pk):
    savat = Savat.objects.get(id=pk)
    savat.miqdor -= 1
    savat.narx = savat.mahsulot.narx * savat.miqdor
    savat.save()
    return redirect("savat")

def savat_q(request, pk):
    savat = Savat.objects.get(id=pk)
    savat.miqdor += 1
    savat.narx = savat.mahsulot.narx * savat.miqdor
    savat.save()
    return redirect("savat")



class BuyurtmaView(View):
    def get(self, request):
         return render(request, "page-profile-orders.html")

