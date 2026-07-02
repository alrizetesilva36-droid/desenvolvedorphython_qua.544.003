# Declaração de variáveis
npme = input("informe o nome do aluno: ").title()
nota = float(input("inorme a nota do aluno:").replace(".","."))

#verifica se a nota é válida
if nota>= 0 nota <= 10:
   if nota>= 7:
      print(f"{nome} está aprovado.")
    elif nota>= 5:
      print(f[nome} está de recuperação.")  
    else:
   print(f"Nota de {nome} inválida.")
 else:
 print(f"Nota de {nome} inválida.") 
