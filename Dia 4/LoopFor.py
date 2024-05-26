lista = ['a','b','c','d','e','f','g','h','i','j']

for letra in lista:
    numero_letra = lista.index(letra) + 1
    print(f"Letra: {letra} : {numero_letra}")

lista = ['pablo','laura', 'julia', 'fede', 'luis']

for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('nombre que no comienza con n')

numeros = [1,2,3,4,5]
mi_valor = 0

for numero in numeros:
    mi_valor = numero + mi_valor
    print(mi_valor)

palabra = 'python'

for letra in palabra:
    print(letra)

for letra in 'python':
    print(letra)

for letra in [[1,2],[3,4],[5,6]]:
    print(letra)

for a,b in [[1,2],[4,5,]]:
    print(a,b)

dic = {'clave1':'a','clave2':'b','clave3':'c'}

for item in dic.items():
    print(item)

for item in dic:
    print(item)

for  a,b in dic.items():
    print(a,b)