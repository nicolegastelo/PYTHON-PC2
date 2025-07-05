numeros = []

while True:
    respuesta = input("¿Desea ingresar un número?: ").strip().lower()
    
    if respuesta == "no":
        break
    elif respuesta == "si":
        entrada = input("Ingrese el número: ").strip()
        try:
            numero = int(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor, ingrese un número válido.")
    else:
        print("Responda con 'SI' o 'NO'.")


pares = 0
impares = 0

for n in numeros:
    if n % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"Números ingresados: {numeros}")
print(f"Cantidad de números pares:{pares}")
print(f"Cantidad de números impares:{impares}")