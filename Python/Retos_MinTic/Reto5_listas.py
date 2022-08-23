def funcion1(x):
    figuritas=[]
    [figuritas.append(item) for item in x if item not in figuritas]
    return figuritas

print(funcion1(['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla']))

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