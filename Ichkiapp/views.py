from django.db.models import Sum
from django.shortcuts import render, redirect
from django.views import View


from  .models import *
from Alistyleapp.models import *

from Userapp.models import Account


class TanlanganView(View):
    def get(self, request):
        a = Account.objects.get(user=request.user)
        tanlangan = Tanlangan.objects.filter(account=a)
        data = {

            "tanlanganlar": tanlangan
        }
        return render(request, "page-profile-wishlist.html", data)

class Tanlangan_ochirView(View):
    def get(self,request, pk):
        Tanlangan.objects.get(id=pk).delete()
        return redirect("tanlangan")


class Tanlangan_QoshView(View):
    def get(self, request, pk):
        m = Mahsulot.objects.get(id = pk)
        a = Account.objects.get(user=request.user)
        tanlangan = Tanlangan.objects.filter(mahsulot=m)
        if len(tanlangan)==0:
            Tanlangan.objects.create(
                mahsulot = m,
                account = a,
            )
        return redirect("savat")

class SavatView(View):
    def get(self, request):
        ac = Account.objects.get(user=request.user)
        savatlar = Savat.objects.filter(account=ac)
        ch = [s.mahsulot.chegirma*s.miqdor for s in savatlar]
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
        account = Account.objects.get(user=request.user)
        data = {
            "buyurtmalar":Buyurtma.objects.filter(account = account)
        }
        return render(request, "page-profile-orders.html", data)

class BuyurtmaQoshView(View):
    def get(self, request):
        account = Account.objects.get(user=request.user)
        savatlar = Savat.objects.filter(account=account)
        b1 = Buyurtma.objects.create(
            account = account,
            mah_narx = savatlar.aggregate(Sum('narx'))["narx__sum"],
            umumiy_narx = savatlar.aggregate(Sum('narx'))["narx__sum"]+5000
        )
        for s in savatlar:
            b1.savat.add(s)
        b1.save()
        return redirect("buyurtma")


