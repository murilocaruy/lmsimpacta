from datetime import datetime

from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

# Create your views here.
def index(request):
    hoje = datetime.now()
    context = {
        'ano': hoje.year + 1,
        'semestre': 1 if hoje.month >= 6 else 2
    }
    return render(request, "index.html", context)

def contato(request):
    context = {}
    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Sua mensagem foi enviada com sucesso') 
        else:
            messages.error(request, 'Problemas ao enviar seu e-mail!')
    else:
        form = ContatoForm()

    context["form"] = form
    return render(request, 'contato.html', context)