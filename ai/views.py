from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from usuarios.models import Cliente
from .models import Pergunta

@csrf_exempt
def chat(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'chat.html', {'cliente': cliente})
    elif request.method == 'POST':
        pergunta = request.POST.get('pergunta')
        pergunta_obj = Pergunta(pergunta=pergunta, cliente=cliente)
        pergunta_obj.save()
        return JsonResponse({'id': pergunta_obj.id, 'pergunta': pergunta_obj.pergunta})