# importação da biblioteca
import os

# laço de retição
while True:
    # limpa tela do terminal
    os.system("cls" if os.name == "nt" else "clear")

    # entrada de dados
    nome = input("informe o nome: ").strip().title() 
    idade = int(input("Informe a idade: "))
    cpf = input("informe o cpf: ").strip()
    email = input("informe o e-mail: ").strip().lower()

    os.system("cls" if os.name == "nt" else "clear")

    # saida de dados
    print(f"Nome: {nome}.")
    print(f"Idade: {idade}.")
    print(f"CPF: {cpf}.")
    print(f"E-mail: {email}.")

    # menu
    print("1 - Informar dados de outro usuário")
    print("2 - Sair do programa")

    opcao = input("Informe a opção desejada: ").strip()

    match opcao:
        case "1":
            continue
        case "2":
            break
        case _:
            print("Opção inválida.")

