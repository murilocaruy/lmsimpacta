from django.shortcuts import render, get_object_or_404

from .models import Curso
# Create your views here.
def curso(request, sigla):
    context= {
        'curso': get_object_or_404(Curso, sigla=sigla)
    }
    return render(request, 'curriculo/curso.html', context)