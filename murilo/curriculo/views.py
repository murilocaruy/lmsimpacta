from django.shortcuts import render

def curso(request, sigla):
    cursos = {
        "SI": {"nome":"Sistemas da Informação", "sigla":"SI", "coordenador":"Osvaldo Kotaro Takai", "descricao":"A Graduação de Sistemas de Informação prepara o aluno para ser um profissional transformador do mercado, desenvolvendo soluções inovadoras e criativas na construção e utilização de Sistemas de Informação. O aluno aprenderá os conceitos teóricos e usos práticos da área, irá acompanhar as principais inovações tecnológicas do mercado e habilitar a sua capacidade empreendedora. O objetivo é formar profissionais capazes de atuar na área de Tecnologia da Informação, criando práticas tecnológicas para determinar o fluxo de informações com o desenvolvimento de software e no gerenciamento de sistemas informatizados. Ao final do 2.º ano, os alunos já terão o diploma de Tecnólogo em Análise e Desenvolvimento de Sistemas."},
        "ADS": {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS", "coordenador":"Ana Cristina dos Santos", "descricao":"Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, aplicação e mensuração de resultados. O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação também estão entre os aprendizados da graduação."},
        "BD": {"nome":"Banco de Dados", "sigla":"BD", "coordenador":"Ana Cristina dos Santos", "descricao":"O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas de desenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área. A graduação mostra a importância da segurança de compartilhamento de dados nas empresas modernas e ensina as melhores técnicas e ferramentas de criação e implementação da mesma. Na Impacta, você será preparado para o cenário real de gestão e liderança empresarial, garantindo a capacidade de comunicação e criatividade para solucionar problemas, atingir os melhores resultados, aumentar a produtividade e reduzir custos."}
    }

    grade = {
        "SI": {"Linguaguem de Programação I","Lógica de Programação"},
        "ADS": {"Linguaguem de Programação I","Lógica de Programação"},
        "BD": {"Linguaguem de Programação I","Lógica de Programação"}

    }

    context = {
        "atual": cursos[sigla], "grade": grade[sigla],
    }
    return render(request, "curriculo/curso.html", context)


def disciplina(request, sigla):
    disciplinas = {
        "LP1": {"nome":"X", "descricao":"Y", "ementa":"Z"},
        "LP": {"nome":"X", "descricao":"Y", "ementa":"Z"},
        "IOT": {"nome":"X", "descricao":"Y", "ementa":"Z"},
        "CE": {"nome":"X", "descricao":"Y", "ementa":"Z"},
        "FBD": {"nome":"X", "descricao":"Y", "ementa":"Z"},
    }

    context = {
        "detalhes": disciplinas[sigla]
    }
    return render(request, "curriculo/disciplina.html", context)