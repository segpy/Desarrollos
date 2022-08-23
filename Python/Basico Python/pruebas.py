#%%
import math
#recibir una entrada del usuario
k=0
while k==0:
    numero = int(input())
    #numero_prueba = 65


    a = 'catalina me dijo: \'hola\''
    
    entero = 10
    lista = [1,2,3,4,5]
    rango = range(1,10)
    print(math.sin(math.pi/2))
    print(a)
    print(len(a))
    
    for i in a:
        print(i, end="")
#%%
b='catalina'
c='me dijo'
print(b,c,sep='hola',end=' ')
print(c,end=',')
print(b)

#%%
texto='hola mundo'
print('texto sin upper:',texto)
print('texto con upper:',texto.upper())

#%%
ent1,ent2,ent3,ent4 = map(int,input('Ingrese enteros: ').split())
entero = int(input('Ingrese entero'))
entero = int(input('Ingrese entero'))
entero = int(input('Ingrese entero'))
entero = int(input('Ingrese entero'))
entero = int(input('Ingrese entero'))
listas = list([int(input('Ingrese lista')) for i in range(11)])

#%%
valores = [int(x) for x in input().split()]
print(valores)
type(valores)

#%%
x,y,z,n = (int(input()) for i in range (4))
print([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=n])

#%%

#%%
#Programa que imprime la serie de fibonacci
def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a,' Iteraicon: ',i)
        print(b,' Iteraicon: ',i)
        a, b = b, a + b
fibonacci(10)
#%%
#Programa que grafica un seno con matplotlib
import matplotlib.pyplot as plt
import numpy as np
def sin(x):
    return np.sin(x)
x = np.arange(0, 6, 0.1)
y = sin(x)
plt.plot(x, y)
plt.show()

#%%
#prubea tecnica de arreglos
lista = [[1,2], [[3,4]], [5, []]]
print(lista)

def flat (lista):
    #crear lista vacia
    lista_vacia = []
    for item in lista:
        for subitem in item:
            if type(subitem) == list:
                #pregunta si el subitem es vacio
                if subitem == []:
                    lista_vacia.append([])
                for subsubitem in subitem:
                    lista_vacia.append(subsubitem)
            else:
                lista_vacia.append(subitem)
    return lista_vacia
print(flat(lista))









