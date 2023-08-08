from django.shortcuts import render,redirect
from .models import Dados
from django.http import HttpResponse
import re
import string
import random
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required

def ir(request):
    return render (request,'home.html')
def ir_login(request):
    return render (request,'login.html')
def ir_muda(request):
    return render (request, 'change.html')

def criar(request):
    nome = request.POST.get('nome')
    mail = request.POST.get('mail')
    senha1 = request.POST.get('senha1')
    senha2 = request.POST.get('senha2')
    
    if senha1 != senha2:
        return render (request, 'home.html',{'mensagem':'Erro! senhas diferentes'})
    
    se=re.compile(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$#%]).{6,}$")
    b=se.fullmatch(senha1)
    if not b:
        return render (request, 'home.html',{'mensagem':'Erro! formato de senha invalido'})

    padrao=re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
    a=padrao.fullmatch(mail)
    if not a:
        return render (request, 'home.html',{'mensagem':'Erro! e-mail invalido'})
    
    
    
    if  Dados.objects.filter(nome=nome).exists():
        return render (request, 'home.html',{'mensagem':'Erro! usuario já registrado'})

    
    

    chars=string.ascii_uppercase + string.digits
    toke=''.join(random.choice(chars) for _ in range(5))

    dado=Dados(
        nome=nome,
        e_mail=mail,
        senha=senha1,
        codigo=toke
    )

    dado.save()
    
    dados=Dados.objects.get( nome = nome)
    
    
    send_mail('confirme seu cadstro',f'Bom dia,{nome}. Confirme seu cadastro com o token: {toke}','josealexandrebarros1990@hotmail.com',[mail])

    return render (request, 'mail.html',{'dados':dados})


def toke(request,id):
    dados=Dados.objects.get( id = id)
    toke = request.POST.get('toke')
    if toke==dados.codigo:
        Dados.objects.filter(id=id).update(ativado=True)
        Dados.objects.filter(id=id).update(codigo='nulo')
        return render (request, 'mail.html',{'dados':dados,'mensagem':'Cadastro realizado com sucesso'})
    else:
        return render (request, 'mail.html',{'dados':dados,'mensagem':'Token errado'})
    
def login(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')

    if  Dados.objects.filter(logado=True).exists():
        return render (request,'login.html',{'mensagem':'um usuario já está logado,faça logout'})

    if not Dados.objects.filter(nome=nome).exists():
        return render (request,'login.html',{'mensagem':'usuario não cadastrado'})
    
    dados=Dados.objects.get( nome = nome)
    if senha != dados.senha:
        return render (request,'login.html',{'mensagem':'senha invalida'})
    if dados.ativado==False:
        return render (request,'login.html',{'mensagem':'senha invalida'})
    Dados.objects.filter(nome=nome).update(logado=True)
    return render (request,'login.html',{'mensagem':'Logado'})
        
    
def mudar(request):
    nome = request.POST.get('nome')
    senha = request.POST.get('senha')
    if not Dados.objects.filter(nome=nome).exists():
        return render (request,'change.html',{'mensagem':'usuario não cadastrado'})
    dados=Dados.objects.get(nome=nome)
    if not dados.logado:
        return render (request,'change.html',{'mensagem':'usuario não logado'})
    
    
    
    se=re.compile(r"^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$#%]).{6,}$")
    b=se.fullmatch(senha)
    if not b:
        return render (request, 'change.html',{'mensagem':'Erro! formato de senha invalido'})
    Dados.objects.filter(nome=nome).update(senha=senha)
    return render (request,'change.html',{'mensagem':'senha alterada'})

def logout(request):
    Dados.objects.filter(logado=True).update(logado=False)
    return render (request, 'login.html',{'mensagem':'Logout realizado'})