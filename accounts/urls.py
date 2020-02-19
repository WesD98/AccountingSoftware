from django.contrib.auth import views
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.indexView, name='index'),
    path('dashboard/', views.dashboardView, name='dashboard'),
    path('login/', LoginView.as_view(template_name = 'accounts/registration/login.html'), name = 'login'),
    path('register/', views.registerView, name='register_url'),
    path('logout/', LogoutView.as_view(next_page = 'dashboard'), name='logout'),
    path('profile/', views.profileView, name='profile_url'),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='accounts/registration/password_change_done.html'), name='password_change_done'),
    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='accounts/registration/password_change.html'), name='password_change'),
    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='accounts/registration/password_reset.html'), name='password_reset'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/registration/password_reset_complete.html'), name='password_reset_complete'),
]