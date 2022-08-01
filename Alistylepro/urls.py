from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Alistyleapp.views import *
from Userapp.views import *
from Ichkiapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Asosiy.as_view(), name="asosiy"),
    path('home/', Homeview.as_view(), name="home"),
    path('bolimlar/', BolimlarView.as_view(), name="bolimlar"),
    path('mahsulot/<int:pk>/', MahsulotView.as_view(), name="mahsulot"),
    path('bolimlar/<int:pk>/', IchkiView.as_view(), name="ichki"),
    path('ichki/<int:pk>/', IchkiBolimView.as_view(), name="ichki_id"),
    path('login/', Loginview.as_view(), name="login"),
    path('register/', Regview.as_view(), name="register"),
    path('tanlangan/', TanlanganView.as_view(), name="tanlangan"),
    path('tanlangan_ochir/<int:pk>/', Tanlangan_ochirView.as_view(), name="tanlangan_ochir"),
    path('tanlangan_qosh/<int:pk>/', Tanlangan_QoshView.as_view(), name="tanlangan_qosh"),
    path('savat/', SavatView.as_view(), name="savat"),
    path('savat_k/<int:pk>/', savat_k, name="savat_k"),
    path('savat_q/<int:pk>/', savat_q, name="savat_q"),
    path('savat/<int:pk>/', SavatQoshView.as_view(), name="savat_qosh"),
    path('buyurtma/', BuyurtmaView.as_view(), name="buyurtma"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
