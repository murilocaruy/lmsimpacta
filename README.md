# Projeto LMS - Parte 1

Esse repoitório contém o que deve ser necessário para a primeira entrega do projeto LMS. A primeira entrega consiste nos layouts do site, o projeto inicial e as suas aplicações.

## Aplicações

Como visto em aula, é razoável que qualquer projeto construído via Django seja dividido em diversas menores aplicações, facilitando a manutenção e reforçando a separação de responsabilidades. Nesse sentido, vamos deixar já criados todos as aplicações do projeto:

 * *site*: Aplicação principal, todas as configurações gerais, templates bases e arquivos comuns devem estar aqui dentro. Não deve haver nenhuma grande regra de negócio aqui.
 * *contas*: Aplicação de contas de sistema, que gerenciará os nossos três tipos de usuários (Aluno, Professor e Coordenador).
 * *curriculo*: Aplicação que cuida do currículo do sistema. Toda o cadastro de cursos, disciplinas e turmas será feito aqui.
