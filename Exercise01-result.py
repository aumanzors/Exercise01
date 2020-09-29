#creando la lista vacia
listaRegistro = []
clientes = 0
clientela = int(input("Clientes a ingresar: "))
costoTotal=0
while clientes < clientela:
    
    cliente = input("nombre del cliente: ")
    producto = input("nombre del producto: ")
    costo = float(input("costo($0.00): "))

    #registro: {"cliente": cliente, "producto": producto, "costo": costo}
    registro = dict(cliente=cliente, producto=producto, costo=costo)
    #print(registro)
    #print(type(registro))

    #agregar nuevo elemento a una lista
    listaRegistro.append(registro)
    #dejar de ocupar la variable registro
    #registro=none
    clientes += 1
for registro in listaRegistro:
    costoTotal+=registro.get("costo")
    print(registro)

print("El costo total de los productos es de: "+ str(costoTotal))
    
    
    