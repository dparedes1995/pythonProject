palabra = 'python'

lista = [letra for letra in palabra]
lista = [n for n in range(0,21,2)]
lista = [n/2 for n in range(0,21,2)]
lista = [n if n * 2 >10 else 'no' for n in range(0,21,2) ]
print(lista)

pies = [10,20,30,40,50,60,70,80,90]
metros = [p * 3.281 for p in pies]

print(metros)