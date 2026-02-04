import datetime

class Pergunta:
    def __init__ (self,id,enunciado,alternativas,alternativa_correta):
        self.id = id
        self.enunciado = enunciado
        self.alternativas = alternativas
        self.alternativa_correta = alternativa_correta

class Quiz:
    def __init__(self,id,titulo,lista_de_perguntas):
        self.id = id
        self.titulo = titulo
        self.lista_de_perguntas = lista_de_perguntas

class Resultado:
    def __init__(self,id,Quiz,nome_participante,nota,data):
        self.id = id
        self.quiz = Quiz
        self.nome_participante = nome_participante
        self.nota = nota
        self.data = data