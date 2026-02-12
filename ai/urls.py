from django.urls import path
from . import views

urlpatterns = [
    path("chat/<int:id>", views.chat, name='chat'),
    path("stream_resposta/", views.stream_resposta, name='stream_resposta'),
    path("ver_referencias/<int:id>", views.ver_referencias, name='ver_referencias'),
    path("analise_jurisprudencia/<int:id>", views.analise_jurisprudencia, name='analise_jurisprudencia'),
    path("processar_analise/<int:id>", views.processar_analise, name='processar_analise'),
    path("webhook_whatsapp/", views.webhook_whatsapp, name='webhook_whatsapp'),
    path("gerar_pdf_analise/<int:id>", views.gerar_pdf_analise, name='gerar_pdf_analise'),
]