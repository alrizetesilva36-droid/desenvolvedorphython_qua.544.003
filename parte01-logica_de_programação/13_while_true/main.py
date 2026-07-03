# taratamento de exceção 
try:
    while True:
        nome = input("informe o nome: ").strip().title()
        idade = int(input("informe a idade: "))
        altura = float(input("informe a altura em metros: ").replace(",","."))

        if idade >= 12 and altura >= 1.25:
            print(f"{nome} está liberado.")    
        else:
            print(f"Entrada de {nome} proibida.")

            print("1 - Passar novo pagante.")
            print("2 - Encerrar programa.")

            opção = input("infomea opação desejada: ").strip()

            match opção:
                case "1":
                    continue
                case "2":
                    print("programa encerrado.")
                    break
                case _:
                    continue
                
except:
    print("Não foi possível registrar a entrada do pagante.")