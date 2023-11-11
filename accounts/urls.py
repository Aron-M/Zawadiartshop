from django.urls import path
from . import views
from .views import CustomLogoutView


urlpatterns = [
    path('login/', views.custom_login_view, name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('welcome_back/', views.welcome_back, name='welcome_back'),
    path('signup/', views.register_view, name='signup'),
    path('profile/', views.user_profile, name='user_profile'),
    path('update_address/', views.update_user_address, name='update_address'),
]