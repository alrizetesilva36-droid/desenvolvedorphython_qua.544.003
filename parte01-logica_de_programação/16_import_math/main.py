# importação de biblioteca
import math

# tratamento de exceção
try:
    while True:
        # usuário informa o valor do raio
        r = float(input("informe o valor do raio em m²: ").replace(",","."))

        # calcula a área do circulo
        area = math.pi*r**2

        # imprime na tela a área do circulo
        print(f"Área do circulo:{area:.2f} m².")

        # usuário informa se deseja continuar ou não
        print("1 - Calcular área deoutro círculo")
        print("2 - Sair do programa")

        opcao = input("Informe sua opção: ").strip()

        match opcao:
            case "1":
                continue
            case "2":
                break
            case _:
                print("opção inválida.")
                continue        
except Exception as e:
    print(f"Não foi possivel calcular.{e}.")
