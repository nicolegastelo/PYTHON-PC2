meses = [
    "Enero",
    "Febrero",
    "Marzo",
    "Abril",
    "Mayo",
    "Junio",
    "Julio",
    "Agosto",
    "Septiembre",
    "Octubre",
    "Noviembre",
    "Diciembre"
]

fecha = input("Ingrese una fecha: ")

if "/" in fecha:
    partes = fecha.split("/")
    mes = int(partes[0])
    dia = int(partes[1])
    anio = int(partes[2])
else:
    partes = fecha.replace(",", "").split()
    mes_nombre = partes[0]
    dia = int(partes[1])
    anio = int(partes[2])
    mes = meses.index(mes_nombre) + 1


print(f"{anio}-{mes:02}-{dia:02}")