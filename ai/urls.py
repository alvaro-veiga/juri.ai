from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:id>", views.chat, name='chat'),
    path("stream_response/", views.stream_response, name='stream_response'),
]