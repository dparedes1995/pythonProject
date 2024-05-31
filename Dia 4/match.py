serie = 'N-02'

if serie=='N-02':
    print('Samsung')
elif serie=='N-03':
    print('Motorola')
elif serie=='N-04':
    print('Nokia')
else:
    print('No existe Producto')

match serie:
    case 'N-02':
        print('Samsung')
    case 'N-03':
        print('Motorola')
    case 'N-04':
        print('Nokia')
    case _:
        print('No existe Producto')

cliente = {'nombre':'Federico', 'apellido':'Gordi', 'email':'abd@gmail.com', 'edad':21, 'ocupacion':'instructor'}
pelicula = {'titulo': 'Matrix', 'ficha_tecnica':{'protagonista':'Kanu reves', 'director':'lana y lily'}}
elementos = [cliente, pelicula, 'libro']

for elemento in elementos:
    match elemento:
        case {'nombre':nombre, 'apellido':apellido, 'email':email, 'edad':edad, 'ocupacion':ocupacion}:
            print('Es un cliente')
            print(nombre, apellido, email, edad, ocupacion)
        case {'titulo':titulo, 'ficha_tecnica': {'protagonista':protagonista, 'director':director}}:
            print('Es un pelicula')
            print(titulo,protagonista,director)
        case _:
            print('Nose que es esto')