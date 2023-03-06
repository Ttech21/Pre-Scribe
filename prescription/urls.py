from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", views.home,name='home'),
    path("registration", views.register_user,name='registration'),
    path("login/", views.login_user,name="login"),
    path("logout/", views.logout_user,name="logout"),
    path("profile/", views.profile,name="profile"),
    path("profile-edit/", views.profile_edit,name="profile-edit"),

    path("prescription-create/", views.prescription_create,name="prescription-create"),
    path("prescription-update/<str:pk>/", views.prescription_update,name="prescription-update"),

    path("medicine-bulk-add/", views.medicine_bulk_add,name="medicine-bulk-add"),
    path("advice-bulk-add/", views.advice_bulk_add,name="advice-bulk-add"),


    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='prescription/change-password.html'), name='change_password'),
    path('change-password-done/', auth_views.PasswordChangeDoneView.as_view(
        template_name='prescription/change-password-done.html'), name='password_change_done'),

    path('reset_password/', auth_views.PasswordResetView.as_view(
        template_name='prescription/reset-password.html'), name='password_reset'),

    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(
        template_name='prescription/reset-password-sent.html'), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='prescription/reset-password-page.html'), name='password_reset_confirm'),

    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(
        template_name='prescription/reset-password-complete.html'), name='password_reset_complete')

]