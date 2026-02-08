from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from usuarios.models import Cliente

@csrf_exempt
def chat(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == 'GET':
        return render(request, 'chat.html', {'cliente': cliente})