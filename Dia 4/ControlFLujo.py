mascota = 'gato'

if mascota == 'gato':
    print('Tienes un gato')
elif mascota == 'perro':
    print('Tienes un perro')
else:
    print('No se que animal tienes')

edad = 18
calificacion = 9
if edad < 18:
    print('Eres menor de edad')
    if calificacion >= 7:
        print('Aprobado')
    else:
        print('Reprobado')
else:
    print('Eres mayor de edad')