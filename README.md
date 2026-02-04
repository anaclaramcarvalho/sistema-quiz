*PROJETO QUIZ - SISTEMA DE GESTÃO DE QUESTIONÁRIOS*

Este sistema foi desenvolvido como parte da disciplina de LIPAI (Linguagem de Interface para Programas de Inteligência Artificial). O objetivo é gerenciar o ciclo de vida de questionários interativos, desde o cadastro de perguntas até a análise de desempenho dos usuários.

*DESCRIÇÃO DO PROBLEMA*

Sistemas de quiz exigem a organização de dados estruturados e relacionais (Perguntas <-> Quizzes <-> Resultados). Este projeto resolve a necessidade de persistir esses dados de forma simples em arquivos CSV, permitindo que professores ou administradores criem conteúdos dinâmicos e estudantes respondam e acompanhem seus resultados sem a necessidade de um banco de dados complexo.

*FUNCIONALIDADES PRINCIPAIS*

Cadastro de Perguntas: Criação de enunciados com 4 alternativas e indicação de resposta correta.

Montagem de Quizzes: Seleção dinâmica de perguntas cadastradas para compor um novo Quiz temático.

Modo de Resposta: Interface para o aluno responder ao quiz, com feedback imediato de acerto/erro.

Registro de Resultados: Armazenamento automático do nome do aluno, nota final e carimbo de data/hora (timestamp).

Histórico de Desempenho: Visualização formatada de todos os resultados salvos no sistema.
