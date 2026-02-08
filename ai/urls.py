from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:id>", views.chat, name='chat'),
]