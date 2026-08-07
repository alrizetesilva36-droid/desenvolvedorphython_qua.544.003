# lista de dicionários
usuários = [
    {
        'nomes': "Fulano",
        'idade': 18,
        'imail': "fulano@gmail.com"
    },
    {
        'nomes': "cicrano",
        'idade': 21,
        'email': "cicrano@gmail.com"
    },
    {
     'nomes': "beltrano",
     'idade': 21,
     'email': "beltrano@gmail.com"
     }
]

# percorre a lista de dicionários
for usuário in usuários:
    for chave, valor in usuário.items():
        print(f"{chave.capitalize()}: {valor}")
    print(f"{'-'*40}")    
    
    
 