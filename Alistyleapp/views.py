from django.shortcuts import render
from django.views import View
from .models import *

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
        return render(request, "ichki.html", data)