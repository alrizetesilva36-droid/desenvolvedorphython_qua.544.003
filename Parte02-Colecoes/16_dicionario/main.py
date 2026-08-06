# dicionário
usuario = {
'nome': "Fulano de Tal",
'idade': 35,
'email': "fulano@gmail.com",
'cpf': "123.456.789-12"
}

# exibe os dados do dicionário
print(f"Nome: {usuario['nome']}")
print(f"Idade: {usuario['idade']}")
print(f"Email: {usuario['email']}")
print(f"CPF: {usuario['cpf']}")


# forma 2
print(f"Nome: {usuario.get('nome')}")
print(f"Idade: {usuario.get('idade')}")
print(f"Email: {usuario.get('email')}")
print(f"CPF: {usuario.get('cpf')}")

# forma 3
print("forma 3:")
for chave in usuario:
    print(f"{chave.capitalize()}: {usuario.get(chave)}")
