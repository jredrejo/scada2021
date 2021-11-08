from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('prueba', views.prueba, name="prueba"),
    path('info', views.info, name="info"),
    path('tag/<int:pk>/', views.detalle_tag, name='detalle_tag'),
    path('seno', views.seno, name='senoidal'),
    path('descargar', views.descargar, name='descarga'),
    path('tabla', views.tabla, name='tabla'),
    path('grafica', views.grafica, name='grafica'),
    path('datosgrafica', views.datos_grafica, name='datos_grafica'),
]