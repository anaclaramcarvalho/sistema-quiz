import os
from repositorios import *
from models import Pergunta, Quiz,Resultado
from datetime import datetime

def cadastrar_perguntas():
    print("\n*=*=*=*=* CADASTRO DE PERGUNTA =*=*=*=*=*=*")
    enunciado = input("Digite o enunciado da pergunta: ")
    alternativas = []
    letras = ['A','B','C','D']
    for letra in letras:
        alternativa = input(f"Digite o texto da  alternativa {letra}: ")
        alternativas.append(alternativa)
    correta = input("Qual a letra da alternativa correta? ").upper()
    
    perguntas_existentes = carregar_perguntas()
    novo_id = len(perguntas_existentes) + 1
    nova_pergunta = Pergunta(novo_id,enunciado,alternativas,correta)
    
    salvar_perguntas(nova_pergunta)
    print("Pergunta cadastrada com sucesso!")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

def montar_quiz():
    print("\n*=*=*=*=* MONTAGEM DE QUIZ =*=*=*=*=*=*")
    todas = carregar_perguntas()
    if not todas:
        print("Erro: Você precisa cadastrar perguntas antes de montar um quiz!")
        return
    titulo = input("Título do Quiz: ")
    for p in todas:
        print(f"[{p.id}] -> {p.enunciado}")
    selecionadas = []
    while True:
        id_escolhido = input("Digite o ID da pergunta para adicionar ela ou S para salvar: ")
        if id_escolhido.upper() == 'S':
            if len(selecionadas) > 0 :
                break
            else:
                print("Pelo menos uma pergunta precisa ser adicionada")
                continue
        pergunta_encontrada = None
        for p in todas:
            if str(p.id) == id_escolhido:
                pergunta_encontrada = p
                break
        if pergunta_encontrada:
            selecionadas.append(pergunta_encontrada)
            print(f"Pergunta {pergunta_encontrada.enunciado} adicionada !!")
        else:
            print("ID não encontrado. Tente novamente.")
    quizzes_existentes = carregar_quiz()
    novo_id_quiz = len(quizzes_existentes) + 1
    novo_quiz = Quiz(novo_id_quiz, titulo,selecionadas)
    salvar_quiz(novo_quiz)
    print(f"Quiz {titulo} criado com sucesso!!")
    print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")

def responder_quiz():
    lista_quiz = carregar_quiz()
    if not lista_quiz:
        print("Nenhum quiz encontrado.")
        return
    print("\n*=*=*=*=* QUIZZES DISPONÍVEIS =*=*=*=*=*=*")
    for q in lista_quiz:
        print(f"[{q.id}] {q.titulo}")
    id_escolhido = input("Digite o ID do quiz que deseja responder: ")
    quiz_atual = None
    for q in lista_quiz:
        if str(q.id) == id_escolhido:
            quiz_atual = q
            break
    if quiz_atual:
        nota = 0
        nome_aluno = input("Digite seu nome: ")
        for p in quiz_atual.lista_de_perguntas:
            print(f"\nPergunta: {p.enunciado}")
            print(f"A) {p.alternativas[0]}")
            print(f"B) {p.alternativas[1]}")
            print(f"C) {p.alternativas[2]}")
            print(f"D) {p.alternativas[3]}")
            resposta = input("Sua resposta é ").upper()
            if resposta == p.alternativa_correta:
                print("ACERTOU!!!")
                nota += 1
            else:
                print(f"VOCÊ ERROU, A RESPOSTA CERTA ERA {p.alternativa_correta}")
        print(f"\n{nome_aluno}, você acertou {nota} de {len(quiz_atual.lista_de_perguntas)}") 
        data_finalizada = datetime.now().strftime("%d/%m/%Y %H:%M") 
        resultados_existentes = carregar_resultados()
        novoID_resposta = len(resultados_existentes) + 1
        novo_resultado = Resultado(novoID_resposta, quiz_atual,nome_aluno,nota,data_finalizada)

        salvar_resultado(novo_resultado)

def ver_resultados():
    dados = carregar_resultados()
    print("\n" + "=*"*20 + " RESULTADOS " + "=*"*20)

    if not dados:
        print("Não tem resultados registrados")
    else:
        for r in dados:
            print(f"Nome: {r[1]:<15} | QUIZ: {r[2]:<20} | Nota: {r[3]:<3} | Data: {r[4]}")
    print("=*"*64)

# ************* MENU PRINCIPAL******************
def menu():
    while True:
        print("\n" + "#"*30)
        print("SISTEMA DE QUIZ")
        print("#"*30)
        print("1. Cadastrar Pergunta")
        print("2. Montar Quiz")
        print("3. Responder Quiz")
        print("4. Ver Resultados")
        print("0. Sair")
        opcao = input("\nEscolha uma opção: ")
        if opcao == "1":
            cadastrar_perguntas()
        elif opcao == "2":
            montar_quiz()
        elif opcao == "3":
            responder_quiz()
        elif opcao == "4":
            ver_resultados()
        elif opcao == "0":
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    menu()