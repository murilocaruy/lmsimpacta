from django.shortcuts import render

from .forms import ContatoForm, LoginForm

# Create your views here.
def home(request):
    context = {
        "titulo":"Outro Título",
    }
    return render(request, "index.html", context)

def contato(request):
    context = {}

    if request.POST:
        form = ContatoForm(request.POST)
        if form.is_valid():
            context["mensagem"] = "Mensagem enviada com sucesso"
        else:
            context["mensagem"] = "Problemas ao enviar a mensagem"
    else:
        form = ContatoForm()
        context["mensagem"] = "Foi um GET"

    context["form"] = form
    return render(request, "contato.html", context)

def login(request):
    context = {}

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            context["mensagem"] = "Bem vindo"
        else:
            context["mensagem"] = "Não foi possível logar"
    else:
        form = ContatoForm()

    context["form"] = form
    return render(request, "login.html", context)