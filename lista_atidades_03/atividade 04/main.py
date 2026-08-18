import operacoes

def exibir_menu():
    print("\n--- MENU DE OPÇÕES ---")
    print("1. Calcular Potência")
    print("2. Calcular Raiz Quadrada")
    print("3. Calcular Volume de Paralelepípedo")
    print("4. Calcular Volume de Cilindro")
    print("5. Limpar Terminal")
    print("0. Sair")
    print("----------------------")

def programa_principal():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            base = float(input("Digite a base: "))
            expoente = float(input("Digite o expoente: "))
            resultado = operacoes.calcular_potencia(base, expoente)
            print(f"Resultado: {base} ^ {expoente} = {resultado}")

        elif opcao == "2":
            num = float(input("Digite o número: "))
            resultado = operacoes.calcular_raiz_quadrada(num)
            if resultado is None:
                print("Erro: Não existe raiz quadrada de número negativo nos reais.")
            else:
                print(f"A raiz quadrada de {num} é {resultado:.2f}")

        elif opcao == "3":
            c = float(input("Digite o comprimento: "))
            l = float(input("Digite a largura: "))
            a = float(input("Digite a altura: "))
            resultado = operacoes.volume_paralelepipedo(c, l, a)
            print(f"O volume do paralelepípedo é: {resultado:.2f}")

        elif opcao == "4":
            r = float(input("Digite o raio da base: "))
            a = float(input("Digite a altura: "))
            resultado = operacoes.volume_cilindro(r, a)
            print(f"O volume do cilindro é: {resultado:.2f}")

        elif opcao == "5":
            operacoes.limpar_terminal()
            print("Terminal limpo!")

        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break
            
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    programa_principal()
