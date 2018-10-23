

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
            {"nome":"Linguaguem de Programação I", "sigla":"LP1"},
            {"nome":"Lógica de Programação", "sigla":"LP"},
            {"nome":"Introdução a Internet das Coisas - IOT", "sigla":"IOT"},
            {"nome":"Comunicação e Expressão (EAD)", "sigla":"CE"},
            {"nome":"Fundamentos de Banco de Dados", "sigla":"FBD"},
        ]
    }