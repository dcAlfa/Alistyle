from django.db import models
from Userapp.models import Account

class Bolim(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to="rasmlar", blank=True)

    def __str__(self):
        return self.nom

class Ichki(models.Model):
    nom = models.CharField(max_length=50)
    rasm = models.FileField(upload_to="rasmlar")
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True, related_name="bolim_ichkilari")

    def __str__(self):
        return self.nom

class Mahsulot(models.Model):
    nom = models.CharField(max_length=50)
    narx = models.PositiveSmallIntegerField()
    ishlab_ch = models.CharField(max_length=100)
    kafolat = models.CharField(max_length=60)
    yetkazish = models.CharField(max_length=50)
    olchov = models.CharField(max_length=10, blank=True)
    min_buyurtma = models.CharField(max_length=10, blank=True)
    mavjud = models.BooleanField(default=True)
    batafsil = models.TextField()
    chegirma = models.PositiveSmallIntegerField(default=0)
    ichki = models.ForeignKey(Ichki, on_delete=models.SET_NULL, null=True, related_name="ichki_mahsulotlar")

    def __str__(self):
        return self.nom

class Media(models.Model):
    rasm = models.FileField()
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True, related_name="mahsulot_medialar")

    def __str__(self):
        return self.mahsulot

class Comment(models.Model):
    mijoz = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True

                                 )
    izoh = models.CharField(max_length=300)
    baho = models.PositiveSmallIntegerField(default=4)
    sana = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.izoh
