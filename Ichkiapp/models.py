from django.db import models

from Alistyleapp.models import *

from Userapp.models import *


class Tanlangan(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE  , related_name="mahsulot_tanlangan")
    account = models.ForeignKey(Account, on_delete=models.CASCADE )

class Savat(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    miqdor = models.PositiveSmallIntegerField(default=1)
    narx = models.PositiveSmallIntegerField()
    chegirma = models.PositiveSmallIntegerField(default=0)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

class Buyurtma(models.Model):
    sana = models.DateField(auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    savat = models.ManyToManyField(Savat)
    mah_narx = models.PositiveSmallIntegerField()
    yet_narx = models.PositiveSmallIntegerField()
    umumiy_narx = models.PositiveSmallIntegerField()
