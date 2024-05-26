nombre = input("Ingrese el nombre: ")
ventas = input("Ingrese el monto de ventas que realizo: ")
comision = round(float(ventas) * 13 / 100, 2)

print(f"Hola {nombre}, su pago de comisiones por las ventas {ventas} soles, es {comision}")
