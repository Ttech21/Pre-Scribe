from django.urls import path
from . import views

urlpatterns = [
    path("add-medicine/", views.add_medicine,name='add-medicine'),
    path("medicine-list/", views.all_medicine,name='medicine-list'),
    path("advice-list/", views.all_advice,name='advice-list'),
    path("investigation-list/", views.all_investigation,name='investigation-list'),
]
