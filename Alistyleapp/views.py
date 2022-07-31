from django.shortcuts import render, redirect
from django.views import View
from .models import *
from Userapp.models import Account

from Ichkiapp.models import *


class Asosiy(View):
    def get(self,request):
        data = {
            "bolimlar": Bolim.objects.all()[:8]
        }
        return render(request, "page-index-2.html", data)

class Homeview(View):
    def get(self,request):
        data = {
            "bolimlar": Bolim.objects.all()[:8]
        }
        return render(request, "page-index.html", data)

class BolimlarView(View):
     def get(self,request):
         data = {
             "bolimlar": Bolim.objects.all()
         }
         return render(request, "page-category.html", data)

class IchkiView(View):
    def get(self, request, pk):
        data = {
            "ichkilar": Bolim.objects.get(id=pk).bolim_ichkilari.all()
        }
        return render(request, "ichki.html", data)
class IchkiBolimView(View):
    def get(self, request, pk):
        data = {
            "mahsulotlar": Ichki.objects.get(id=pk).ichki_mahsulotlar.all()
        }
        return render(request, "page-listing-grid.html", data)
class MahsulotView(View):
    def get(self, request,pk):
        m = Mahsulot.objects.get(id = pk)
        s = Savat.objects.filter(mahsulot=m)
        buyurtmalar = Buyurtma.objects.filter(savat__in=s)
        data = {
            "mahsulot": m,
            "comments": Comment.objects.filter(mahsulot=m)[:10],
            "comment_soni": Comment.objects.filter(mahsulot=m).count(),
            "buyurtma_soni": len(buyurtmalar)
        }
        return render(request, "page-detail-product.html", data)
    def post(self,request, pk):
        m = Mahsulot.objects.get(id=pk)
        Comment.objects.create(
            mahsulot = m,
            mijoz = Account.objects.get(user = request.user),
            izoh = request.POST.get("c")
        )
        return redirect("mahsulot", pk)
