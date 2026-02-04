import csv 
from models import Pergunta, Quiz, Resultado
import os

def salvar_perguntas(pergunta):
    caminho = 'data/perguntas.csv'
    if not os.path.exists('data'):
        os.makedirs('data')
        caminho = 'data/perguntas.csv'
    with open(caminho, mode = 'a', newline = '',encoding = 'utf-8')as arquivo:
        escritor = csv.writer(arquivo)
        linha = [
            pergunta.id,
            pergunta.enunciado,
            pergunta.alternativas[0],
            pergunta.alternativas[1],
            pergunta.alternativas[2],
            pergunta.alternativas[3],
            pergunta.alternativa_correta
        ]
        escritor.writerow(linha)

def carregar_perguntas():
    perguntas = []
    caminho = 'data/perguntas.csv'
    if not os.path.exists(caminho):
        return [] 
    with open(caminho, mode = 'r',encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            alts = [linha[2],linha[3],linha[4],linha[5]]
            p = Pergunta(int(linha[0]),linha[1],alts,linha[6])
            perguntas.append(p)
    return perguntas

def salvar_quiz(quiz):
    caminho = 'data/quizzes.csv'
    if not os.path.exists('data'):
        os.makedirs('data')
    ids = []
    for p in quiz.lista_de_perguntas:
        id_str = str(p.id)
        ids.append(id_str)
    ids_formatados = ";".join(ids)
    with open(caminho, mode = 'a', newline = '',encoding = 'utf-8')as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([quiz.id,quiz.titulo,ids_formatados])

def carregar_quiz():
    perguntas = carregar_perguntas()
    caminho = 'data/quizzes.csv'
    quizzes = []
    if not os.path.exists(caminho):
        return [] 
    with open(caminho, mode = 'r',encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            id_quiz = int(linha[0])
            titulo = linha[1]
            ids_string = linha[2].split(';')
            perguntas_selecionadas = []
            for id_buscado in ids_string:
                for p in perguntas:
                    if(str(p.id) == id_buscado):
                        perguntas_selecionadas.append(p)
            novo_quiz = Quiz(id_quiz,titulo,perguntas_selecionadas)
            quizzes.append(novo_quiz)
    return quizzes

def salvar_resultado(novo_resultado):
    caminho = 'data/resultados.csv'
    if not os.path.exists('data'): 
        os.makedirs('data')
    with open(caminho, mode = 'a', newline = '',encoding = 'utf-8')as arquivo:
        escritor = csv.writer(arquivo)
        linha = [
            novo_resultado.id,
            novo_resultado.nome_participante,
            novo_resultado.quiz.titulo,
            novo_resultado.nota,
            novo_resultado.data
        ]
        escritor.writerow(linha)

def carregar_resultados():
    caminho = 'data/resultados.csv'
    if not os.path.exists(caminho):
        return []
    resultados = []
    with open (caminho, mode = 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            resultados.append(linha)
    return resultados