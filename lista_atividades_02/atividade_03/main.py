import json
import os

# Nome do arquivo JSON onde os dados serão salvos
aluno_json = "alunos.json"

# Tenta carregar dados existentes para não apagar o arquivo anterior
try:
    if os.path.exists(aluno_json):
        with open(aluno_json, "r", encoding="utf-8") as f:
            dados_alunos = json.load(f)
    else:
        dados_alunos = []
except json.JSONDecodeError:
    dados_alunos = []

# Laço para cadastrar os alunos
while True:
    nome = input("Digite o nome do aluno: ")
    
    # Recebe as 3 notas
    nota1 = float(input("Digite a nota 1: "))
    nota2 = float(input("Digite a nota 2: "))
    nota3 = float(input("Digite a nota 3: "))
    
    # Calcula a média
    media = (nota1 + nota2 + nota3) / 3
    
    # Verifica aprovação
    if media >= 7:
        situacao = "Aprovado"
    else:
        situacao = "Reprovado"
        
    # Mostra o resultado na tela
    print(f"Média: {media:.2f} - Situação: {situacao}")
    
    # Cria o dicionário com os dados do aluno atual
    aluno = {
        "nome": nome,
        "notas": [nota1, nota2, nota3],
        "media": round(media, 2),
        "situacao": situacao
    }
    
    # Adiciona na lista geral
    dados_alunos.append(aluno)
    
    # Pergunta se deseja continuar
    continuar = input("Deseja inserir notas de outro aluno? (s/n): ").strip().lower()
    if continuar != 's':
        break

# Grava todos os dados acumulados no arquivo JSON
with open(nome_alunos, "w", encoding="utf-8") as f:
    json.dump(dados, f, ensure_ascii=False, indent=4)

print(f"Dados salvos com sucesso em '{nome_alunos}'!")


