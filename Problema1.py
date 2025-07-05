resultados = []

for numero in range(1500, 2701):
    if (numero % 7 == 0) and (numero % 5 == 0):
        resultados.append(numero)


print("Números divisibles por 7 y múltiplos de 5 entre 1500 y 2700:")
print(resultados)