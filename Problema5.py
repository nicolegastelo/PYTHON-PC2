numero = int(input("Ingrese un número entero: "))
digito = input("Ingrese el dígito a buscar: ")

if len(digito) != 1 or not digito.isdigit():
    print("Debe ingresar un solo dígito del 0 al 9.")
else:
    numero_str = str(abs(numero))
    cantidad = numero_str.count(digito)
    print(f"Cantidad de veces que '{digito}' aparece en el número {numero}: {cantidad}")