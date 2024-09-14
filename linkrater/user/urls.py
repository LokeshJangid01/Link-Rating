from django.urls import path
from django.contrib.auth.views import LoginView


from .views import signup

app_name = 'user'

urlpatterns = [
    path('signup/',signup, name = 'signup'),
    path('login/',LoginView.as_view(template_name = 'user/login.html'), name = 'login'),
    
]