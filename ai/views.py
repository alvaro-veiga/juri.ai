from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from usuarios.models import Cliente
from .models import Pergunta
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .agent import JuriAI
from typing import Iterator
from agno.agent import RunOutputEvent, RunEvent
from django.http import StreamingHttpResponse

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
def stream_resposta(request):
    id_pergunta = request.POST.get('id_pergunta')

    pergunta = get_object_or_404(Pergunta, id=id_pergunta)

    def gerar_resposta():
        
        agent = JuriAI.build_agent(knowledge_filters={'cliente_id': pergunta.cliente.id})
        
        stream: Iterator[RunOutputEvent] = agent.run(pergunta.pergunta, stream=True, stream_events=True)
        for chunk in stream:
            if chunk.event == RunEvent.run_content:
                yield str(chunk.content)

    response = StreamingHttpResponse(
        gerar_resposta(),
        content_type='text/plain; charset=utf-8'
    )
    response['Cache-Control'] = 'no-cache'
    response['X-Accel-Buffering'] = 'no'
    
    return response