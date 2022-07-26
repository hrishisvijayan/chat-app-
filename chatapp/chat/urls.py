from django.urls import path,include
from . import views

urlpatterns = [
    path('chat',views.home),
    path('',views.lobby)

]