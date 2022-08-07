from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_user/', views.edit_user, name='edit_user')

]
