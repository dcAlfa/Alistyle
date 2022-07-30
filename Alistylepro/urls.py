from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Alistyleapp.views import *
from Userapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Asosiy.as_view(), name="asosiy"),
    path('home/', Homeview.as_view(), name="home"),
    path('bolimlar/', BolimlarView.as_view(), name="bolimlar"),
    path('bolimlar/<int:pk>/', IchkiView.as_view(), name="ichki"),
    path('ichki/<int:pk>/', IchkiBolimView.as_view(), name="ichki_id"),
    path('login/', Loginview.as_view(), name="login"),
    path('register/', Regview.as_view(), name="register"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
