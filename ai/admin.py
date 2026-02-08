from django.contrib import admin
from .models import Pergunta, ContextRag, AnaliseJurisprudencia

# Register your models here.
admin.site.register(Pergunta)
admin.site.register(ContextRag)
admin.site.register(AnaliseJurisprudencia)
