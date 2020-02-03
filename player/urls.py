from django.urls import path, re_path
from .views import home 
from django.contrib.auth.views import LoginView, LogoutView

app_name='player'
urlpatterns = [
    re_path(r'login$', LoginView.as_view(template_name = 'player/login_form.html'), name = 'player_login'),
    re_path(r'logout$', LogoutView.as_view(), name = 'player_logout'),
    re_path(r'home/$', home, name = 'player_home'),
]

