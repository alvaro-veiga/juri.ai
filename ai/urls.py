from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:id>", views.chat, name='chat'),
    path("stream_resposta/", views.stream_resposta, name='stream_resposta'),
]