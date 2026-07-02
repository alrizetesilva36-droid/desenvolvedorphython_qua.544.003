# declaração de variáveis
nome = input("informe seu nome:").title()
idade = int(input("informe sua idade:"))

#saida de dados com opérador ternário
print(f"{nome} é maior de idade." if idade >= 18 else f"{nome} é menor de idade. ")
