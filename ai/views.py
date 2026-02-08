from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from usuarios.models import Cliente
from .models import Pergunta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .agent import JuriAI

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

@csrf_exempt
def stream_response(request):
    id_pergunta = request.GET.get('id_pergunta')
    pergunta = get_object_or_404(Pergunta, id=id_pergunta)

    agente = JuriAI.build_agent()
    resposta = agente.print_response(pergunta.pergunta)
    return JsonResponse({'resposta': resposta})