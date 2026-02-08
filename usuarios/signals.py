from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documentos
from ai.tasks import ocr_and_markdown_file, rag_documentos
from django_q.tasks import async_task

@receiver(post_save, sender=Documentos)
def save_documents(sender, instance, created, **kwargs):
    
    async_task(ocr_and_markdown_file, instance.id)

    rag_documentos(instance.id)