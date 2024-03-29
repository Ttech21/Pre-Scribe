from django.urls import path
from . import views
urlpatterns = [
    path("", views.register_user,name='registration'),
    path("login/", views.login_user,name="login"),
    path("logout/", views.logout_user,name="logout"),


    path("prescription-create/", views.prescription_create,name="prescription-create"),
    path("profile/", views.profile,name="profile"),
    path("medicine-bulk-add/", views.medicine_bulk_add,name="medicine-bulk-add"),
    path("advice-bulk-add/", views.advice_bulk_add,name="advice-bulk-add"),
]