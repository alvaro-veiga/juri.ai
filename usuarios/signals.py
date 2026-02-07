from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documentos
from ai.tasks import ocr_and_markdown_file
@receiver(post_save, sender=Documentos)
def save_documents(sender, instance, created, **kwargs):
    ocr_and_markdown_file()