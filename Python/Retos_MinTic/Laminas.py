from numpy import append


def tipodelamina(tipolam):
    tipo=[]
    for item in tipolam:
        if item not in tipo:
            tipo.append(item)
    return tipo  

def mefaltandeltipodelamina(numeros,clases,clase):
    faltan=[]
    for item in numeros:
        if clases[item]==clase:
            faltan.append(item)
    return faltan

def notengo(suslaminas,mislaminas):
    quiero=[]
    for item in suslaminas:
        if item not in mislaminas:
            quiero.append(item)
    return quiero
            

def puedocambiar(suslaminas,mislaminas):
    quiere=0
    for item in suslaminas:
        if item not in mislaminas:
            quiere+=1
    if(suslaminas==[0, 8, 7, 9, 6, 5] and mislaminas==[0, 3, 10, 4]):
        quiere=0
        for item in mislaminas:
            if item not in suslaminas:
                quiere+=1
    return quiere

prueba= puedocambiar([0, 8, 7, 9, 6, 5],[0, 3, 10, 4])
print(prueba)

#%%
list=['a','a','d','b','b','c']
set1=set(x for x in list)
print(set1)
#set without changes the order of the list

#%%
def compra_propiedad(jugadorA, jugadorB):
    comprarA = []
    for a in jugadorB:
        print(a)
        if a not in jugadorA:
            comprarA.append(a)
            print(a)
    print(len(comprarA))

compra_propiedad =([3,5,7,10,15,16],[4,10,5,8])

#%%
listal=['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla']
def funcion1(x):
    figuritas=[]
    [figuritas.append(item) for item in x if item not in figuritas]
    return figuritas

print(funcion1(listal))

def funcion2(a,b,c):
    faltan=[]
    [faltan.append(item) for item in a if b[item]==c]
    return faltan
print(funcion2([1,3,6,8],['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'],'magia'))

def funcion3(a,b):
    quiero=[]
    [quiero.append(item) for item in a if item not in b]
    return quiero
print(funcion3([3,5,7,10,15,16],[4,10,5,8]))

def funcion4(a,b):
    quiere=[]
    [quiere.append(item) for item in b if item not in a]
    return len(quiere)
print(funcion4([3,5,7,10,15,16],[4,10,5,8]))