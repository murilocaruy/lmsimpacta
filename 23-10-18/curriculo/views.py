from django.shortcuts import render

def curso(request, sigla):
    cursos = {
        "SI": {"nome":"Sistemas da Informação", "sigla":"SI", "coordenador":"Osvaldo Kotaro Takai", "descricao":"A Graduação de Sistemas de Informação prepara o aluno para ser um profissional transformador do mercado, desenvolvendo soluções inovadoras e criativas na construção e utilização de Sistemas de Informação. O aluno aprenderá os conceitos teóricos e usos práticos da área, irá acompanhar as principais inovações tecnológicas do mercado e habilitar a sua capacidade empreendedora. O objetivo é formar profissionais capazes de atuar na área de Tecnologia da Informação, criando práticas tecnológicas para determinar o fluxo de informações com o desenvolvimento de software e no gerenciamento de sistemas informatizados. Ao final do 2.º ano, os alunos já terão o diploma de Tecnólogo em Análise e Desenvolvimento de Sistemas."},
        "ADS": {"nome":"Análise e Desenvolvimento de Sistemas", "sigla":"ADS", "coordenador":"Ana Cristina dos Santos", "descricao":"Entender as necessidades das empresas é fundamental para fazê-las crescer e gerar bons resultados. Desta maneira, um dos caminhos para alavancar os negócios e se destacar no mercado de trabalho é o da Tecnologia. Para isso, a Faculdade Impacta oferece a graduação em Análise e Desenvolvimento de Sistemas, que prepara você para atuar em todas as etapas de projetos de tecnologia da informação - concepção, gerência e manutenção, aplicação e mensuração de resultados. O curso é voltado para a criação de programas, softwares e sistemas para as empresas. As etapas do projeto de sistemas de software, como análise, projeto, teste, gestão, implantação e manutenção de sistemas de informação também estão entre os aprendizados da graduação."},
        "BD": {"nome":"Banco de Dados", "sigla":"BD", "coordenador":"Ana Cristina dos Santos", "descricao":"O curso de Banco de Dados prepara o aluno para ser um profissional versátil e com habilidades para atuar com diversas plataformas e estruturas de desenvolvimento e administração de sistemas de Banco de Dados, com acesso a todo o repertório técnico e teórico da área. A graduação mostra a importância da segurança de compartilhamento de dados nas empresas modernas e ensina as melhores técnicas e ferramentas de criação e implementação da mesma. Na Impacta, você será preparado para o cenário real de gestão e liderança empresarial, garantindo a capacidade de comunicação e criatividade para solucionar problemas, atingir os melhores resultados, aumentar a produtividade e reduzir custos."}
    }

    context = {
        "atual": cursos[sigla]
    }
    return render(request, "curriculo/curso.html", context)


def disciplina(request, sigla, abrev):
    disciplinas = {
        "LP1": {"nome":"Linguaguem de Programação I", "abrev":"LP1", "descricao":"Introdução e Conceitos de Programação e Linguagem de Programação.", "ementa":"Linguagem de Programação Python. Tipos de Dados. Estruturas lógicas ou de controle de fluxo. Modularização. Métodos. Classes. Desenvolvimento de projeto IoT."},
        "LP": {"nome":"Lógica de Programação", "abrev":"LP", "descricao":"Introdução à Lógica e aos Algoritmos.", "ementa":"Tipos de Dados. Estruturas lógicas ou de controle de fluxo. Modularização. Introdução às Estruturas de Dados. Estruturas de Dados Homogêneas. Métodos de Busca (Busca Linear e Busca Binária). Métodos de Ordenação (Métodos Bolha, Inserção e Seleção)."},
        "IOT": {"nome":"Introdução a Internet das Coisas - IOT", "abrev":"IOT", "descricao":"Introdução à computação ubíqua. Desenvolvimento de soluções IoT.", "ementa":"Tipos de transdutores, sensores e atuadores. Componentes básicos do computador e dispositivos de Internet das coisas (Arduino). Funcionalidades dos subsistemas de memória, unidade central de processamento, barramentos e sistema de entrada/saída. Processos, sistemas de arquivos e drivers."},
        "CE": {"nome":"Comunicação e Expressão (EAD)", "abrev":"CE", "descricao":"A fluência na língua materna possibilita a plena compreensão dos textos indicados e a excelência na produção cientifica.", "ementa":"Aplicação prática da expressividade ao falar em público, com direcionamento acadêmico e empresarial. Desenvolvimento de textos corporativos e científicos. Leitura crítica e interpretativa. Elaboração de textos, permeados pela clareza, intencionalidade, coesão e coerência. Orientação para emprego da ABNT em produções científicas."},
        "FBD": {"nome":"Fundamentos de Banco de Dados", "abrev":"FBD", "descricao":"Introdução aos Sistemas Gerenciadores de Banco de Dados.", "ementa":"Projeto de Banco de Dados. Projeto Conceitual de Banco de Dados: Modelo Entidade Relacionamento: UML: Uso de Diagramas de Classes da UML para representar as Abstrações de Generalização, Agregação e Composição. Projeto Lógico de Banco de Dados: Modelo Relacional; Normalização."},
    }

    context = {
        "detalhes": disciplinas[abrev]
    }
    return render(request, "curriculo/disciplina.html", context)