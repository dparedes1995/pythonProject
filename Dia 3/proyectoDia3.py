texto = input("Ingrese el texto que desea enviar: ")
letras = input("Ingrese 3 letras que desea enviar: ")
texto = texto.lower()
letras = letras.lower()
if len(letras) !=3 : exit("Debe ingresar 3 letras")
for letra in letras:
    print(f"La letra {letra} se encuentra en el texto {texto.find(letra) + 1} veces")

print(f"En el texto hay {len(texto)} letras")
print(f"La primera letra del Texto es la letra {texto[0]} y la ultima letra es {texto[-1]}")
print(f"El texto al reves seria {texto[-1::-1]}")
if "phyton" in texto:
    print(f"La palabra Phyton se encuentra en el texto")
else:
    print(f"La palabra Phyton no se encuentra en el texto")