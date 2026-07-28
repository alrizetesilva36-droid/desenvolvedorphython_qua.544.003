import sys

# Cadastro inicial do usuário
nome = input("Digite seu nome: ").strip()
idade = int(input("Digite sua idade: "))

# Lista de filmes com classificação indicativa e sala
filmes = {
    "1": {"titulo": "A volta dos que não foram", "idade_min": 0, "sala": "Sala 1"},
    "2": {"titulo": "A Roda Quadrada", "idade_min": 12, "sala": "Sala 2"},
    "3": {"titulo": "As Tranças do Rei Careca", "idade_min": 14, "sala": "Sala 3"},
    "4": {"titulo": "Poeira em Alto Mar", "idade_min": 16, "sala": "Sala 4"},
    "5": {"titulo": "A vingança do Frango Assado", "idade_min": 18, "sala": "Sala 5"}
}

while True:
    # Exibição do catálogo de filmes
    print("\n=== FILMES EM CARTAZ ===")
    for opcao, info in filmes.items():
        classificacao = "Livre" if info["idade_min"] == 0 else f"{info['idade_min']} anos"
        print(f"[{opcao}] {info['titulo']} ({classificacao}) - {info['sala']}")
    
    # Escolha do usuário
    escolha = input("\nEscolha o número da sala/filme desejado: ").strip()
    
    # Validação da opção escolhida
    if escolha not in filmes:
        print("Opção inválida! Escolha uma sala existente.")
        continue
        
    filme_escolhido = Screen_info = filmes[escolha]
    
    # Verificação de idade
    if idade < filme_escolhido["idade_min"]:
        print(f"\n[ACESSO NEGADO] Você tem {idade} anos e não tem a idade mínima "
              f"({filme_escolhido['idade_min']} anos) para assistir a este filme.")
        print("Por favor, selecione outro filme.")
    else:
        # Gravação do bilhete em arquivo de texto
        nome_arquivo = "bilhete_cinema.txt"
        with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
            arquivo.write("=== BILHETE DE CINEMA ===\n")
            arquivo.write(f"Cliente: {nome}\n")
            arquivo.write(f"Idade: {idade} anos\n")
            arquivo.write(f"Filme: {filme_escolhido['titulo']}\n")
            arquivo.write(f"Local: {filme_escolhido['sala']}\n")
            arquivo.write("=========================\n")
            
        print(f"\n[SUCESSO] Entrada autorizada! Seu bilhete foi gravado em '{nome_arquivo}'.")
        print("Tenha um ótimo filme!")
        sys.exit() 
         # Encerra o programa

