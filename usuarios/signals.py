from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Documentos
from ai.tasks import ocr_and_markdown_file, rag_documentos
from django_q.tasks import Chain

@receiver(post_save, sender=Documentos)
def save_documents(sender, instance, created, **kwargs):
    if created:
        chain = Chain()
        chain.append(ocr_and_markdown_file, instance.id)
        chain.append(rag_documentos, instance.id)
        chain.run()