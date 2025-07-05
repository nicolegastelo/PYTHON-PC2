texto = input("Ingrese un texto: ")

vocales = "aeiouAEIOU"

sin_vocales = ""

for caracter in texto:
    if caracter not in vocales:
        sin_vocales += caracter


print(f"Texto sin vocales:{sin_vocales}")