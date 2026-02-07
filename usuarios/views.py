from django.shortcuts import render, redirect
from django.contrib.messages import constants
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def cadastro(request):
    if request.method == 'GET':
        # Garante que a sessão existe
        request.session.modified = True
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')
        
        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'Senha e confirmar senha não são iguais.')
            return redirect('cadastro')
            
        if len(senha) < 6:
            messages.add_message(request, constants.ERROR, 'Sua senha deve ter pelo menos 6 caracteres.')
            return redirect('cadastro')

        users = User.objects.filter(username=username)
        
        if users.exists():
            messages.add_message(request, constants.ERROR, 'Já existe um usuário com esse username.')
            return redirect('cadastro')
        
        User.objects.create_user(
            username=username,
            password=senha
        )
        
        messages.add_message(request, constants.SUCCESS, 'Usuário cadastrado com sucesso!')
        return redirect('login')