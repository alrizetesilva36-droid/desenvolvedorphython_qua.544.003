# declaração de variáveia 
x = float(input("informeo valor de x: ").replace(",","."))
y = float(input("infome o valor de y: ").replace(",","."))

# menu
print("1 - Somar")
print("2 - Subtrair")
print("3 - Mulitiplicar")
print("4 - Dividir")

opção = input("informe a opção desejada: ").strip()

match opção:
    case "1":
        print(f"A soma é {x+y}.")
    case "2":
        print(f"A subtração é {x-y}.")
    case "3":
        print(f"A multiplicação é{x*y}.")
    case "4":
        print(f" A divisão é {x/y}.")
    case _:
        print("opção inválida.")