cidades =[
    "Brasília",
    "Rio de Janeiro",
    "Belo Horizonte"
    "São Paulo",
    "Goiânia",
    "Manaus",
    "Fortaleza",
    "Florianópolis"
]

cidade_pesquisada = input("Informe o nome da cidade a ser pesquisada: ").strip().title()

# mostra a posição di item da lista
if cidade in cidades:
    indice = cidades.index(cidade)
    print(f"Indice de {cidade} na lista é {indice}.")
else:
    print("Cidade não encontrada")

