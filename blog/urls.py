from django.urls import path
from . import views

urlpatterns = [
    path('', views.publicacion_lista, name ='publicacion_lista'),
    path('publicaciones/<int:pk>', views.publicacion_detalle, name ='publicacion_detalle'),

]