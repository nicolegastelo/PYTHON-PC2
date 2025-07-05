def factorial(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado

numero = int(input("Ingrese un número entero no negativo: "))
resultado = factorial(numero)
print(f"El factorial del número es:{resultado}")