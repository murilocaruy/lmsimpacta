from curriculo.models import Curso

def lista_cursos(request):
    return {
        "cursos":[
            {"nome":"Sistemas da Informação", "sigla":"SI"},
            {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS"},
            {"nome":"Banco de Dados", "sigla":"BD"},
        ]
    }

def lista_disciplinas(request):
    return {
        "disciplinas":[
            {"nome":"Linguaguem de Programação I", "abrev":"LP1"},
            {"nome":"Lógica de Programação", "abrev":"LP"},
            {"nome":"Introdução a Internet das Coisas - IOT", "abrev":"IOT"},
            {"nome":"Comunicação e Expressão (EAD)", "abrev":"CE"},
            {"nome":"Fundamentos de Banco de Dados", "abrev":"FBD"},
        ]
    }