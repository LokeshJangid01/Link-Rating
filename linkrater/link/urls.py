from django.urls import path

from .views import add_link,detail, add_review

app_name = 'link'

urlpatterns = [
    path('add/',add_link,name='addlink'),
    path('<int:pk>/',detail,name='detail'),
    path('<int:pk>/add/',add_review,name='add_review'),
]