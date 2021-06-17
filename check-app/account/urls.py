from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('login', views.login, name='login'),
    path('reset_password/', auth_views.PasswordResetView.as_view(),
         name="password_reset"),
    path('reset_password_sent/',
         auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(),
         name="password_reset_confirm"),
    path('reset_password_confirm/', auth_views.PasswordResetCompleteView.as_view(template_name='account/password_reset_complete.html'),
         name="password_reset_complete")
]
