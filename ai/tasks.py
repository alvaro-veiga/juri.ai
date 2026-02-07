from usuarios.models import Documentos
from django.shortcuts import get_object_or_404

def ocr_and_markdown_file(instance_id):
    from docling.document_converter import DocumentConverter

    documento = get_object_or_404(Documentos, id=instance_id)
    