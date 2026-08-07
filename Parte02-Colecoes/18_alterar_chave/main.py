usuario = {
'nome': "Fulano de Tal",
'idade': 35,
'email': "fulano@gmail.com",
'cpf': "123.456.789-12"
}

# usuário informa a chave que deseja alterar
chave = input("Informe o nome da chave: ").strip().lower()
if chave in usuario:
    # usuario informa o novo valor da chave
    usuario[chave] = input("Informe o novo valor para a chave: ").strip()

    # exibe o dicionário com o novo valor da chave escolhida
    for chave,valor in usuario.items():
        print(f"{chave.capitalize()}: {valor}")

else:
    print("chave não encontrada.")

