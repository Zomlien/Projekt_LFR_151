from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login_user/', views.login_user, name="login"),
    path('logout_user/', views.logout_user, name="logout"),
    path('register_user/', views.register_user, name="register_user"),
    path('view_user/', views.view_user, name="user_account"),
    path('password/', auth_views.PasswordChangeView.as_view(
        template_name='/change_password.html',
        success_url='/account/password_change_done'  # Remove the trailing slash here
    ), name="password"),
    path('password_change_done', views.password_change_done, name="password_change_done"),
    path('delete_account/', views.delete_account, name='delete_account'),
]
