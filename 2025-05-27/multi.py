try:
    a = int(input("Digite o primeiro número inteiro positivo: "))
    b = int(input("Digite o segundo número inteiro positivo: "))

    if not (a > 0 and b > 0):
        print("Por favor, digite apenas números inteiros positivos.")
    else:
        produto = 0
        contador = 0
        while contador < b:
            produto += a
            contador += 1
        print("O produto é:", produto)

except ValueError:
    print("Entrada inválida. Por favor, digite números inteiros.")