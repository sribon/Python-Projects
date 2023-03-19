from django.urls import path
from store import views

urlpatterns = [
    path('', views.home, name="home"),
    path('modulos/', views.modulos, name="modulos"),
    path('baterias/', views.baterias, name="baterias"),
    path('fcarga/', views.fcarga, name="fcarga"),
    path('ffrontal/', views.ffrontal, name="ffrontal"),
    path('camaras/', views.camaras, name="camaras"),
    path('extra/', views.extra, name="extra"),
]