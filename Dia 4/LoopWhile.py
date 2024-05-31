monedas = 5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas = monedas - 1
else:print("No tengo mas dinero")

respuesta = 's'

while respuesta == 's':
    respuesta = input("Quieres seguir? (s/n)")
else:
    print("Gracias por usar o programa")

respuesta = 's'

while respuesta == 's':
    pass
else:
    print("Gracias por usar o programa")

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'v':
        break
    print(letra)

nombre = input("Tu nombre: ")

for letra in nombre:
    if letra == 'v':
        continue
    print(letra)