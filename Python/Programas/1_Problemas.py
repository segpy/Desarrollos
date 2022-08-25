# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 11:47:09 2022

@author: sebas
"""
#%%

import numpy as np
import math
import decimal
import random


#PROBLEMAS
#%%
"""
¿Cuál es el número entero que es el cuadrado de un número entero dado?
"""
a = int(input("Ingrese el numero que desea elevar al cuadrado: "))
operacion = a**2
print(f'El cuadrado del numero ingresado es: {operacion}')



#TAREAS
#%%Tarea1: Factura
def round_up(n, decimals=0):
    multiplier = 10 ** decimals
    return math.ceil(n * multiplier) / multiplier

inicio="Si"
while inicio=="Si" or inicio=="si":
    f1=True
    while f1==True:
        a = int(input("Ingrese el porcentaje del IVA: "))
        if (a<0):
            print('ERROR: El valor del IVA no es valido')
        else:
            f1=False
    f2=True
    while f2==True:
        b = int(input("Ingrese el precio unitario con IVA incluido: "))
        if (b<=0):
            print('ERROR: El precio debe ser mayor a 0')
        else:
            f2=False
    f3=True
    while f3==True:
        c = int(input("Ingrese la cantidad como numero entero: "))
        if c<0:
            print('ERROR: Cantidad ingresada no valida')
        else:
            f3=False
    total=b*c
    subtotal=round_up(int(total/(1+(a/100))),-1)
    iva=round_up(int(total-subtotal),-2)
    #Salidas
    print('\nSu factura. ')
    print(f'El subtotal es: {subtotal}')
    print(f'El valor del IVA es: {iva}')
    print(f'El valor total con IVA incluido es: {total} \n')
    inicio = input("¿Desea continuar con una nueva factura?\n Si o No: ")

#%%
#Tarea 2
lambetazo = ["QUERIDOS","APRECIADOS","DISTINGUIDOS","HONORABLES","ESTIMADOS","RESPETADOS"]
potenciales_marranos = ["COMPATRIOTAS", "CONCIUDADANOS", "AMIGOS", "COTERRANEOS","COPARTIDARIOS","ELECTORES"]
condicion = ["EN MI GOBIERNO","CON SU APOYO","SIENDO ELEGIDO", "CON SU AYUDA", "SI ME SIGUEN", "DURANTE MI MANDATO"]
compromiso = ["VOY A DERROTAR","VENCERÉ","ELIMINARÉ","ACABARÉ","LUCHARÉ CONTRA", "COMBATIRE"]
ilusion_guerrerista = ["LA VIOLENCIA Y","LA DELINCUENCIA Y","LA CORRUPCION Y","LA INFLACION Y","LA PROBREZA Y","EL DESPLAZAMIENTO Y"]
promesa = ["TRABAJARÉ POR","GARANTIZARÉ","PROTEGERÉ","VELARÉ POR","PROMOVERÉ","DEFENDERÉ"]
beneficio_populista = ["LA EDUCACIÓN","EL EMPLEO","LA SEGURIDAD","LA LAZ","LA IGUALDAD","LA SALUD"]
cantidad_votos = ["DEL PAIS", "DE LA CIUDAD", "DE LA COMUNIDAD", "DE LA POBLACIÓN", "PARA TODA LA GENTE", "DE CADA COLOMBIANO"]

lambetazo2 = random.choice(lambetazo)
potenciales2 = random.choice(potenciales_marranos)
condicion2 = random.choice(condicion)
compromiso2 = random.choice(compromiso)
ilusion_guerrerista2 = random.choice(ilusion_guerrerista)
promesa2 = random.choice(promesa)
beneficio_populista2 = random.choice(beneficio_populista)
cantidad_votos2 = random.choice(cantidad_votos)

print(f'El discurso elegido es: {lambetazo2} {potenciales2} {condicion2} {compromiso2} {ilusion_guerrerista2} {promesa2} {beneficio_populista2} {cantidad_votos2}')

#%%
n = int(input())
if n%2==0 and (n in range(2,6) or (n>20)):
    print('Not Weird')
else:
    print('Weird')
"""
if n%2==0 and (n in range(2,6) or n>20 ):
    print "Not",

print "Weird"
"""
#%%Reto 1
import math

ale = int(input())
gi = math.floor(2*ale+4)
nico = math.floor((3*gi/10)-2/5)
def etapa(nico):
    if nico>=0 and nico<=20:
        print('uno')
    if nico>20 and nico<=40:
        print('dos')
    if nico>40 and nico<=80:
        print('tres')
    if nico>80:
        print('cuatro')
print(ale,gi,nico)
etapa(nico)

#%%
def maximo_dos_numeros(a, b):
  if a > b:
      return a
  else:
    return b

numero_1 = float(input("Ingrese el primer numero: "))
numero_2 = float(input("Ingrese el segundo numero: "))

print("El numero mayor entre %.2f y %.2f es %.2f" % (numero_1,numero_2,maximo_dos_numeros(numero_1,numero_2)))

#%% Notas
import math
nota1 = float(input('Ingrese la nota 1: '))
nota2 = nota1/2
nota3 = (nota1+nota2)/3
nota4 = (nota1+nota2+nota3)/3

nota_def = ((nota1*0.15)+(nota2*0.2)+(nota3*0.25)+(nota4*0.4))/4
def definitiva(num):
    if num < 6:
        print('Reprobo')
    elif num <= 8:
        print('Bueno')
    else:
        print('Excelente')
definitiva(nota_def)

#%%
import math
import numpy as np

np.array([1,2,3,4,5])
lista = ['a','b','c','d','e']
print(lista)
print(np.pi)


#%%
#Ralice un programa en Python un programa con funciones, que pida
# 1. ¿Cuántos productos va a facturar?
# Solicitar de cada producto Nombre, precio unitario con iva incluido, % del iva y cantidad
cantidad_productos = int(input("¿Cuántos productos va a facturar? "))
totalTotal = subtotalTotal = 0
#Funcion que evalua los siguientes metodos:
#1. Si el total a pagar del valor con iva es superior a 10 millones el 10% del subtotal es el descuento.
#2. Si el total a pagar del valor con iva es superior a 5 millones el 5% del subtotal es el descuento.
#3. Si el total a pagar del valor con iva es superior a 2 millones el 2% del subtotal es el descuento.
#De lo contrario no hay descuento.
def condiciones_total(total,subtotal):
    if total>10000000:
        descuento=subtotal*0.1
    elif total>5000000:
        descuento=subtotal*0.05
    elif total>2000000:
        descuento=subtotal*0.02
    else:
        descuento=0
    return descuento


for i in range(cantidad_productos):
    nombre,precio_unitario,iva, cantidad = input('Nombre del producto'),float(input('Precio unitario con iva incluido')),float(input('% del iva')),int(input('Cantidad'))
    porcent_iva = iva/100
    total=precio_unitario*cantidad
    subtotal=int(total/(1+(iva/100)))
    iva=int(total-subtotal)
    totalTotal += total
    subtotalTotal += subtotal
    print(f'El nombre del producto es: {nombre}',f'La cantidad es: {cantidad}',f'El % del iva es: {porcent_iva}',f'El precio unitario con iva incluido es: {precio_unitario}',f'El subtotal es: {round(subtotal,-2)}',f'El valor del IVA es: {round(iva,-2)}',f'El valor total con IVA incluido es: {total} \n',sep='\n')
    
#Imprimir el total neto
print(f'El subtotal Total es: {round(subtotalTotal,-2)}')
#Imprimir el iva 
print(f'El iva Total es: {round(totalTotal-subtotalTotal,-2)}')
total_neto=totalTotal-condiciones_total(totalTotal,subtotalTotal)
print(f'El total neto es: {total_neto}')

#%%
#flatten an array (list) 
#https://www.geeksforgeeks.org/python-flatten-an-array/
array_toflatten = [[1,2,3],[4,5,6],[7,8,9]]
arreglo2 = [[1,2,3],[4,5,6],[7,8,9]]
array_toflatten2 =[[1,2,3,4],[5,6,7],[8,9],[10]]
print(array_toflatten)

#Metodo 1: List Comprehension
array_flatten = [item for sublista in array_toflatten for item in sublista]
arreglo2_flatten = [j for i in array_toflatten2 for j in i] #i es la sublista y j es el item. Es decir, filas y columnas.
print(f'Arreglo con list comprenhension: {arreglo2_flatten}')

#Metodo 2: For loop anidado
arreglo = []
for sublista in array_toflatten2:
    for item in sublista:
        arreglo.append(item)
print(f'Arreglo con for loop anidado: {arreglo}')


#%% Reto 2
equipo_a = input()
equipo_b = input()
atacar = input()

puntaje_a = 0
puntaje_b = 0

def condiciones(puntajea,puntajeb):
    if puntajea>puntajeb:
        print(f'V',end='')
    elif puntajea<puntajeb:
        print(f'F',end='')
    else:
        print(chr(8776),end='')


for caracter in atacar:
    if caracter in equipo_a:
        puntaje_a += 1
    if caracter in equipo_b:
        puntaje_b += 1
    condiciones(puntaje_a,puntaje_b)
    

#%%Reto 3

#Programa que recibe una lista de caracteres separada por coma
lista = list(input().split(","))
cont = 1
print(lista)
#Toda la lista en mayusculas
lista = [x.upper() for x in lista]
print(lista)
print(len(lista))
listab= []
repetidos=""
print(lista)
#contar las letras consecutivas
for i in range(len(lista)):
    print(f'Iteracion {i}')
    if i!=(len(lista)-1):
        if lista[i]==lista[i+1]:
            cont+=1
            print(lista[i])
        else:
            listab.append(lista[i])
            repetidos=repetidos+str(cont)
            print(lista[i],'no es igual')
            #print(repetidos)
            cont=1
    else:
        print(lista[i])
        listab.append(lista[i])
        repetidos=repetidos+str(cont)
        #print(listab,'no es igual')
        #print(repetidos)
#print(*[x for x in listab])
#print(*[x for x in repetidos])

#%%
#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono y lo guarde en un diccionario. 
#Después debe mostrar por pantalla el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de teléfono es <teléfono>.
diccionario = {}
#ingresar los valores usando dict comprehension
diccionario = {'nombre':input('Ingrese su nombre: '),'edad':input('Ingrese su edad: '),'direccion':input('Ingrese su direccion: '),'telefono':input('Ingrese su telefono: ')}
print(f'{diccionario["nombre"]} tiene {diccionario["edad"]} años, vive en {diccionario["direccion"]} y su número de teléfono es {diccionario["telefono"]}')

#%% Reto 4
import json

diccionario_entrada = input()
#Convertir diccionario string a diccionario usando json.loads
diccionario_entrada1 = json.loads(diccionario_entrada)
diccionario_entrada2 = eval(diccionario_entrada)
print(f'Diccionario entrada 1: {diccionario_entrada1} tipo: {type(diccionario_entrada1)}')
print(f'Diccionario entrada 2: {diccionario_entrada2} tipo: {type(diccionario_entrada2)}')

#print(diccionario_entrada)
#print(type(diccionario_entrada))
laminas_deseadas = input().split()
print(laminas_deseadas)
precio=0
laminas_encontradas=""

for key in laminas_deseadas:
    if key in diccionario_entrada:
        precio += diccionario_entrada[key]
        laminas_encontradas += key + " "
        
print(precio)
print(laminas_encontradas)

#%% Factura v3
#calculos=[]
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

    
#%%
calculos=[[]]
calculos.insert(0,['a','b'])
calculos.append(['a','b'])
print(len(calculos))

#%%Reto 5

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
    for item in mislaminas:
        if item not in suslaminas:
            quiere+=1
    return quiere
    

prueba=tipodelamina(['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'])
print(prueba)
prueba2=mefaltandeltipodelamina([1,3,6,8],['accion','magia','batalla','batalla','batalla','accion','magia','batalla','batalla','batalla'],'magia')
print(prueba2)
prueba3=notengo([3,5,7,10,15,16],[4,10,5,8])
print(prueba3)
prueba4=puedocambiar([3,5,7,10,15,16],[4,10,5,8])
print(prueba4)
#%%
lista=['a','b','c']
lista=[x for x in lista]
listab=[]
print(lista)
for x in lista:
    listab.append(x.upper())
print(lista)
print(listab)

#%%
#Hacer la serie fibonacci
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(10))

#%%
stringprueba = "Protocolo TLS(Transport Layer Security, seguridad)es solo una versión actualizada y más segura de SSL"
#Contar cuantos caracteres hay en la cadena
print(len(stringprueba))


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

#%%
#programa para verificar login de usuario y contraseña usando recursividad
def login(usuario,contrasena,intentos=3):
    if intentos == 0:
        return f'Excedio el numero de intentos'
    elif usuario == 'admin' and contrasena == '1234':
        return f'Bienvenido {usuario}'
    else:
        print('Usuario o contraseña incorrectos')
        usuario = input('Ingrese usuario: ')
        contrasena = input('Ingrese contraseña: ')
        return login(usuario,contrasena,intentos-1)

login(input('Ingrese usuario: '),input('Ingrese contraseña: '))