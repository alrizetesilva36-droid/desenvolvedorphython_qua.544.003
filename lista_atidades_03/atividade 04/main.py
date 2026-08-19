from modulo import limpar,potencia,raiz,volume_cubico,volume_cilindro

def main():
    limpar()
    while True:
        print("1 - Calcular potência")
        print("2 - Calcular raíz")
        print("3 - Calcular volume cúbico")
        print("4 - Calcular volume cilíndrico")
        print("5 - Sair")
        opcao = input("Informe a opção desejada: ").strip()
        limpar()
        match opcao:
            case "1":
                x = int(input("Informe um número inteiro: "))
                y = int(input("Informe a potência: "))
                print(f"{x} elevado a {y} = {potencia(x, y)}")
                continue
            case "2":
                x = int(input("Informe um número inteiro: "))
                print(f"Raíz quadrada de {x} = {raiz(x)}")
                continue
            case "3":
                b = int(input("Informe o valor da base: "))
                l = int(input("Informe o valor da largura: "))
                h = int(input("Informe o valor da altura: "))
                print(f"Volume cúbico é {volume_cubico(b, l, h)}")
                continue
            case "4":
                r = int(input("Informe o valor do raio: "))
                h = int(input("Informe o valor da altura: "))
                print(f"Volume do cilindro é {volume_cilindro(b, h)}")
                continue
            case "5":
                break
            case _:
                print("Opção inválida.")
                continue

if __name__ == "__main__":
    main()
    


            