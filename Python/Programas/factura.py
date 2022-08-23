calculos=[]
productos=[]
cantidad=0 
encontrados=0


def entrada():
    lista_anidada = [int(input("Ingrese el codigo: ")),input("Ingrese el nombre: "),float(input("Ingrese el precio: ")),float(input("Ingrese el porcentaje del iva"))] 
    return lista_anidada



def busqueda(codigo):
    find=0
    global encontrados
    for sublista in productos:
        if codigo == sublista[0]:
            cantidad=int(input("Ingrese la cantidad: "))
            porcent_iva = sublista[3]/100
            calculos.append([sublista[0],int(sublista[2]*cantidad/(1+porcent_iva)),sublista[2]*cantidad-int(sublista[2]*cantidad/(1+porcent_iva)),sublista[2]*cantidad]) # [Codigo,Subtotal,IVA,Total]
            """ print(f'Codigo: {sublista[0]}', end=' ')
            print(f'Nombre: {sublista[1]}', end=' ')
            print(f'Precio: {sublista[2]}', end=' ')
            print(f'IVA: {sublista[3]}', end=' ') """
            """ calculos.append(sublista[2]*cantidad) #Precio total
            calculos.append(int(sublista[2]*cantidad/(1+porcent_iva))) #Subtotal
            calculos.append(sublista[2]*cantidad-int(sublista[2]*cantidad/(1+porcent_iva))) #iva """
            #print(calculos)
            encontrados+=1
            find=1
        else:
            continue
    if find==0:
        print('No se encontro el codigo')

def mostrar():
    for sublista in calculos:
        if sublista[0]:
            print(f'Codigo: {sublista[0]}', end=' ')
            print(f'Subtotal: {sublista[1]}', end=' ')
            print(f'IVA: {sublista[2]}', end=' ')
            print(f'Total: {sublista[3]}')
        else:
            continue
i=True
while i:
    productos.append(entrada())
    if(input("Desea agregar otro producto? (Y/N): ")=='N'):
        i=False

i=True
while i:
    busqueda(int(input("Ingrese el codigo: ")))
    if(encontrados!=len(productos)):
        print(f'Usted ha asignado solamente {encontrados} de {len(productos)} productos')
    else:
        i=False
        break
    if((input("Desea buscar otro producto? (Y/N): ")=='N' and encontrados==len(productos))):
        i=False
        break
    else:
        print("No ha asignado todas las cantidades.")
        
mostrar()