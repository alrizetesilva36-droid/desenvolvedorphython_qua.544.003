def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


numero = int(input("Digite um número inteiro: "))

if numero < 0:
    print("Digite um número maior ou igual a zero.")
else:
    print(f"Sequência de Fibonacci até {numero}:")
    for i in range(numero + 1):
        print(fibonacci(i), end=" ")
    print()
