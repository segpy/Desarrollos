# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 22:55:53 2022

Built-in
programiz.com/python-programming/methods/built-in

String methods
w3schools.com/python/python_ref_string.asp

List methods
https://www.w3schools.com/python/python_ref_list.asp

Dictionary methods
https://www.w3schools.com/python/python_ref_dictionary.asp

Tuple methods
https://www.w3schools.com/python/python_ref_tuple.asp

Set methods
https://www.w3schools.com/python/python_ref_set.asp

File methods
https://www.w3schools.com/python/python_ref_file.asp
"""




#Basico de Python
"""----------------------------------- BUILT-IN FUNCTIONS -----------------------------------"""
#%%  1)     FUNCION PRINT

#Imprimir String
print('Hola mundo')
string='Hola mundo'
print(string)
print(type(string))

#Imprimir entero
entero=10
print(entero,string,sep='',end='')
print('<----No hay endline')

#Imprimir iterables
print(*range(1,6),sep='')

#Imprimir listas
lista = ['a', 'b', 'c', 'd', 'e']
print(lista)
print([a for a in lista])
print(*[a for a in lista])

numeroPi = 3.141516
#imprimir con 2 decimales
print(f'Numero Pi: %.2f' % numeroPi)
print(f'Numero Pi: {numeroPi:.2f}')



#%% 2)      INPUT

#Ingresa un entero 
entero = int(input('Ingrese entero'))

#Ingresa enteros como lista
enteros = [int(input('Ingrese enteros')) for i in range(5)]

#Ingresa enteros como variables (espacio y enter)
ent1,ent2,ent3,ent4 = map(int,input('Ingrese enteros: ').split())
x,y,z,n = (int(input()) for i in range (4))

#Ingresa varias posiciones de una lista (espacio y enter)
arr = list(map(int, input().split()))
listas = list([int(input('Ingrese lista')) for i in range(5)])

#Ingresa una lista anidada
lista_anidada = [[input('Nombre: '), float(input('Nota: '))] for i in range(n)]





"""----------------------------------- TIPOS DE DATOS -----------------------------------"""       
#%%  1)     VARIABLES LOCALES Y GLOBALES

message="How you doing?"
def greet():
    message = "How are you?"
    print("Message inside function", message)

greet()
print("Message outside function:", message)






#%%  2)         TEXTO

text = "He said, \"what\'s there?\""
print(text) #He said, "what's there?"
text1 = "Texto"

#Slicing
print(text1[1:3]) #ex
print(text1[::]) #Texto
print(text1[::-1]) #imprime el texto en reversa (otxeT)
print(text1[4:2:-1]) #Primeras dos posiciones del texto en reversa (ot)
list = ["apple", "banana", "cherry"]
print(list) #['apple', 'banana', 'cherry']
print(list[1]) #banana
print(list[-1]) #cherry
print(list[1:3]) #['banana', 'cherry']
print(list[-3:-1]) #['banana', 'cherry']


#Concatenar string
#Concatenar sin espacio
print(text+text1) #He said, "what's there?"Texto
#Concatenar con espacio
print(text,text1) #He said, "what's there?" Texto
print(text1*3) #TextoTextoTexto

#Control if con texto
text = "PyThOn"
if "P" in text:
    print("P esta en el texto")
else:
    print("P no esta en el texto")

#Iterando
#En print
print([a for a in text1])   #['T', 'e', 'x', 't', 'o']
#En FOR
for a in text1:
    print(a,end=('')) #Texto
print('')

#Metodos/Modulos
#Metodo lower
print(text.upper()) #PYTHON
#Metodo upper
print(text.lower()) #python
#Metodo find
print(text.find('Th')) #2
#Metodo replace
print(text.replace("PyThOn", "Python"))






#%%  3)         {OPERADORES LOGICOS} in | not in | and | or 

text = "Python"
print("P" in text) #True
print([a for a in text]) #['P', 'y', 't', 'h', 'o', 'n']
print("P" and "on" in text) #True
print(("Pyh" or "oN") in text) #False
print("ont" not in text) #True






#%%  4)     LISTAS

#Creacion
lista1= ['a','b','c','d','e']
#Crear lista con list()
lista2 = list(range(5))
#Crear lista con []
lista3 = [1,2,3,4,5]

#Acceder
#Acces items
print(lista1[0]) #a

#Sliciing - #Es como un range(), el ultimo valor es n-1.
print(lista1[1:4]) #['b', 'c', 'd']
print(lista1[::-1]) #['e', 'd', 'c', 'b', 'a']
print(lista1[::2]) #['a', 'c', 'e']
print(lista1[1:]) #['b', 'c', 'd', 'e']
print(lista1[4:2:-1]) #['e', 'd']

#Agregar
#Metodo append
lista1.append('f') #Agrega un elemento al final de la lista
print('Append: ',lista1) #['a', 'B', 'c', 'd', 'e', 'f']
#Metodo insert
lista1.insert(1,'BB') #Inserta un elemento en la posicion 1
print('Insert: ',lista1) #['a', 'BB', 'B', 'c', 'd', 'e', 'f']

#Cambiar
#Change items
lista1[1]='B'

#Iterando
#Iterating through a List
print('B' in lista1) #True
print([a for a in lista1]) #['a','B','c','d','e']
#Metodo count
print('Count:',lista1.count('B')) #Cuenta la cantidad de veces que aparece un elemento en la lista
#Metodo index
print('Index:',lista1.index('e')) #Devuelve la posicion del elemento en la lista

#List comprehensions / Listas anidadas
lista3 = [i for i in range(10)]      #Lista o vector
arreglo2 = [[1,2,3],[4,5,6],[7,8,9]] #Lista anidada o matriz
arreglo2_flatten = [j for i in arreglo2 for j in i] #i es la sublista y j es el item. Es decir, filas y columnas.
print(f'Arreglo con list comprenhension: {arreglo2_flatten}')


#Eliminar
#Metodo pop
lista1.pop() #Elimina el ultimo elemento
print('Pop',lista1)
#Metodo del
del lista1[0] #Elimina el elemento en la posicion 0
print('Del',lista1)
#Metodo remove 
lista1.remove('c') #Elimina el primer elemento que coincida con el valor
print('Remove',lista1)

#Reordenar la lista
#Metodo reverse
lista1.reverse() #Invierte el orden de los elementos
print('Reverse',lista1)
#Metodo sort
lista1.sort() #Ordena los elementos de la lista SOLO SI tienen los mismos tipos de datos
print('Sort',lista1)






#%%  5)        DICCIONARIOS

#Creacion
person1= {"key1":"value1","key2":"value2"}
#Crear diccionario anidado
person3 = {"key1":{"key11":"value11","key12":"value12"},"key2":"value2"}
print('Diccionario anidado: ',person3)
#Crear diccionario con dict()
person4 = dict(key1="value1",key2="value2")
print('Diccionario con dict(): ',person4)


#Diccionario a partir de una lista de tuplas
dic2 = dict([("key1",[1,2,3]),("key2","value2")])
print('Diccionario a partir de una lista de tuplas: ',dic2)
#Diccionario a partir de una lista de listas
dic3 = dict([["key1",[1,2,3]],["key2","value2"]])
print('Diccionario a partir de una lista de listas: ',dic3)
#Diccionario a partir de una lista de listas anidadas
dic4 = dict([["key1",[["key11",1],["key12",2]]],["key2","value2"]])
print('Diccionario a partir de una lista de listas anidadas: ',dic4)
#Diccionario a partir de tuplas de tuplas
dic5 = dict((("key1",1),("key2",2)))
print('Diccionario a partir de tuplas de tuplas: ',dic5)


#Acceder a diccionarios
print(person1["key1"]) #value1
#Metodo get
print(person1.get("key1")) #Devuelve el valor de la key1
print(person1.get("hobbies",["dancing","fishing"])) #['dancing', 'fishing']

#Eliminar
#Metodo pop (elimina keys)
print(person1.pop("key1"), person1) #El valor de la key1 
#Metodo popitem (elimina el ultimo elemento)
person1.popitem() #Elimina el ultimo elemento
print('Popitem',person1)
person1['key1']='value1'
#Metodo del
del person1["key1"] #Elimina la key1
print('Del',person1)

#Crear copia
person1['key1']='value1'
person3 = person1.copy() #Copia el diccionario
person1.popitem()
print('Copia',person3)
print('Original',person1)

#Iterando
person2 = {"key1":"value1","key2":"value2","key3":"value3"}
print([person2[key] for key in person2]) #['value1', 'value2', 'value3']
#Built-in len
print(len(person2)) #Devuelve la cantidad de elementos en el diccionario

#Agregar
#Agregar key y value
person1["keyx"]="valuex"
print(person1) #{'key2': 'value2', 'keyx': 'valuex'}
#Agregar varios values a un solo key
person1["keyx2"]=["valuex2","valuexx2"]
print(person1) #{'key2': 'value2', 'keyx': ['valuex', 'valuexx']}
#Metodo update
person1.update({"keyx3":["valuex3","valuexx3"]})
print('Update:',person1) #Agrego varios valores a un solo key






#%%   6)       SETS

##Creacion
#Crear SET
set1 = {"item1","item2","item3","item4"}
#Crear Set a partir de List
set2 = set(["item1_2","item2","item3","item4_2"])

##Agregar
#Modulo add (agrega 1 item)
set1.add("item5")
#Modulo update (agrega items de seq)
set1.update(set2,{"extraitem"})
print('Update: ',set1)

##Eliminar
#Modulo discard
set1.discard("extraitem")
print('Discard: ',set1)
#Modulo remove
set1.remove("item4_2")
print('Remove: ',set1)
#Modulo clear
set2.clear()
print('Set2: ',set2)

##Iterando
#iteracion for
for item in set1:
    print(item)
#Chekear si
print("item2" in set1)

domestic_animals = {"dog", "cat", "elephant"}
wild_animals = {"lion", "tiger", "elephant"}
#Modulos
#Modulo union -> |
animals = domestic_animals.union(wild_animals)
print(animals)
#Modulo interseccion -> &
common_animals = domestic_animals.intersection(wild_animals)
print(common_animals)






#%%    7)      RANGE FUNCION
print(range(1,11))
print(list(range(1,11)))




#%%    8)      OBJETOS / MODULOS
from ast import main
from mimetypes import init
import random
import math

print('Random: \n',[a for a in dir(random) if "_" not in a])
print('Math: \n',[a for a in dir(math) if "_" not in a])
print('List: \n',[a for a in dir(list()) if "_" not in a])
print('Set: \n', *[a for a in dir(set())  if "_" not in a])
print('String: \n',[a for a in dir(str()) if "_" not in a])
print('Dictionary: \n',[a for a in dir(dict()) if "_" not in a])
print('Int: \n',[a for a in dir(int()) if "_" not in a])
print('Bool: \n',[a for a in dir(bool()) if "_" not in a])
print('Float: \n',[a for a in dir(float()) if "_" not in a])





#%%     9)        MANEJO DE ARCHIVOS - FILES

#Modo w - Escritura (borra el archivo si existe)
#script de escritura
lineas = [
    "Hola mundo",
    "Hola mundo 2",
    "Hola mundo 3"
]
def escribirArchivo(fichero,lineas):
    with open(fichero,"w") as archivo:
        for linea in lineas:
            if not linea.endswith("\n"):
                linea += "\n"
            archivo.write(linea)
escribirArchivo("archivo.txt",lineas)

    
#Modo a - Agregar (escribe al final del documento)
with open('NuevoTexto.txt','a') as f:
    f.write('\nTercera linea creada sobre el mismo texto')
    

#Modo r - Lectura
#script de lectura
def main():
    usuarios = listarUsusarios()
    for usuario in usuarios:
        print(f'Usuario: {usuario}')

def listarUsusarios():
    with open('texto_prueba.txt','r') as f:
        datos = f.readlines()
        users = []
        for linea in datos:
            if linea.startswith('#'):
                continue
            if linea.startswith('_'):
                continue
            if linea.startswith('\n'):
                continue
            users.append(linea.split(':')[0])
        return users


if __name__ == "__main__":
    main()



#Readlines: Lee todas las lineas y las devuelve en una lista
with open('NuevoTexto.txt','r') as f:
    print(f.readlines())
#Readline: Lee una linea y la devuelve como string
with open('NuevoTexto.txt','r') as f:
    print(f.readline())







"""----------------------------- CONTROL DE FLUJO-----------------------------"""
#%%     1)          CONDICIONAL IF
lista1 = [1,2,3]
#CONDICIONAL USANDO OPERADORES LOGICOS
#== igual
a = b = 5
if a==b:
    print('a es igual a b')
#!= diferente
b=3
if a!=b:
    print('a es diferente a b')
#> mayor que
if a>b:
    print('a es mayor que b')
#< menor que
b=6
if a<b:
    print('a es menor que b')
#>= mayor o igual que
b=5
if a>=b:
    print('a es mayor o igual que b')
#<= menor o igual que
b=6
if a<=b:
    print('a es menor o igual que b')
#and y
#or o
#in dentro de
if a in lista1:
    print('a esta dentro de la lista')
#not Negacion
if a not in lista1:
    print('a no esta dentro de la lista')







#%%     2)          ITERACION FOR: str, list, iterable

lista=['a','ab','ac','d','e']
string="holaaxd"
print([i for i in lista if "a" in i]) #['a', 'ab', 'ac']
print([i for i in string])  #['h', 'o', 'l', 'a', 'a', 'x', 'd']
print([i for i in range(10)])   #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(*range(10))  #0 1 2 3 4 5 6 7 8 9







#%%     3)          ITERACION WHILE

i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        break
i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        continue
    print('hola')
    print('adios')
    print('chau')
    #if i==8:
    #    break
i=0
while i<10:
    print(i)
    i+=1
    if i==5:
        continue
    if i==8:
        pass
    if i==9:
        break








#%%     3)          BREAK, CONTINUE y PASS

for i in range(5):
    numero = int(input('Ingrese el numero: '))
    if numero == 3:
        break #Sale del FOR
print('Salimos')

for i in range(5):
    numero = int(input('Ingrese el numero: '))
    if numero == 3:
        continue #Sigue a la siguiente iteracion del FOR
        

for i in range(5):
    numero = int(input('Ingrese el numero: '))
    if numero == 3:
        pass #No hace nada, pasa a la siguiente iteracion







#%%     4)        EXCEPCIONES EN PYTHON
#Try - Except
try: #Se hace siempre
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))

    result = numerator/denominator

    print(result)
    
    my_list = [1, 2, 3]
    i = int(input("Enter index: "))
    print(my_list[i])
#Excepcion -> Se ejecuta si hay un error
#Entra solo si se cumple la excepcion
except ZeroDivisionError: 
    print("Denominator cannot be 0. Try again.")
except IndexError:
    print("Index is wrong.")

print("Program ends")

#Try - Except- Finally
try:
    print(1/0)
except:
    print("Wrong denominator")
finally:
    print("Always printed")
    





"""----------------------------- FUNCIONES -----------------------------"""
#%% 1)      FUNCIONES
#Funcion con parametros como variables y salida print
def sumarayb(a,b):
    return a+b
print(sumarayb(int(input('Ingrese a')), int(input('Ingrese b')))) #a+b


def greet(name, message):
    print("Hello", name)
    print(message)    
greet("Jack", "What's going on?")
greet(message = "Howdy?", name = "Jill")

#Funcion con parametros asignados por defecto y salida return
def add_numbers(n1 = 100, n2 = 1000):
    sum = n1 + n2
    return sum
result = add_numbers(5.4) 
print(result) #Imprime 1005.4


#Funcion recursiva
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(5)) #120

def recursion(n):
    if(n<1):
        return n
    else:
        print(n)
        recursion(n-1)
recursion(5) #5 4 3 2 1

#%%
#Funcion args y kwargs
def greet(*names): #args: convierte el parametro en una tupla
    print(names)
    for name in names:
        print("Posicion", names.index(name), ":", name)
greet("Jack", "Jill", "John", "Mary")

def greet(**names): #kwargs: convierte el parametro en un diccionario
    print(names)
    for name in names:
        print("Hello", name)
greet(Key1 = "Value1", Key2 = "Value2", Key3 = "Value3")

#modificar el valor de una variable dentro de una funcion de manera global
variable = 5
def funcion1(numero):
    valor =2
    global variable
    variable = 10
    print(variable)
    #imprimir todas las variables dentro de la funcion
    print(locals())

def funcion2():
    globals()['variable'] = 20
    print(variable)
funcion1(5) #10
funcion2() #20



"""----------------------------- OBJETOS -----------------------------"""
#%%Objetos
#Crear una clase
class Usuario: #Primera letra en mayuscula
    nombre = 'Felipe'
    apellido = 'Gonzalez'
usuario = Usuario()
print(usuario.nombre) #Felipe

#%%
#Crear clase con constructor y metodos
class Usuario:
    def __init__(self, nombre, apellido): #Constructor
        self.nombre = nombre
        self.apellido = apellido
    def saludar(self): #Self puede ser cualquier nombre
        print('Hola', self.nombre)
usuario = Usuario('Felipe', 'Gonzalez')
usuario.saludar() #Hola Felipe

#Actualizar atributos
usuario.nombre = 'Juan'
usuario.saludar() #Hola Juan

#Eliminar atributos
del usuario.nombre
usuario.saludar() #ERROR
#Eliminar objeto
del usuario

#%%
#Crear clase con constructor y metodos
class Usuario:
    def __init__(self, nombre, apellido): #Constructor
        self.nombre = nombre
        self.apellido = apellido
    def saludar(self): #Self puede ser cualquier nombre
        print('Hola', self.nombre)

#Crear clase con herencia
class Admin(Usuario): 
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido) #Llamar al constructor de la clase padre
    def saludar(self):
        print('Hola', self.nombre, 'Admin')
admin = Admin('Felipe', 'Gonzalez')
usuario = Usuario('Felipe', 'Gonzalez')
usuario.saludar() #Hola Felipe
admin.saludar() #Hola Felipe Admin

#%% Ejercicio herencia
class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
    def hablar(self):
        print('hola soy un', self.tipo, 'mi nombre es', self.nombre,'y mi sonido es', self.sonido)
    #create destructor
    def __del__(self):
        print('Estoy en el destructor de la clase', self.__class__.__name__)


class Perro(Animal):
    tipo = 'perro'

class Gato(Animal):
    tipo = 'gato'

class Pajaro(Animal):
    tipo = 'pajaro'

perro = Perro('Fido', 'Guau')
perro.hablar() #hola soy un perro y mi nombre es Fido
gato = Gato('Garfield', 'Miau')
gato.hablar() #hola soy un gato y mi nombre es Garfield
pajaro = Pajaro('Polly', 'Piu')
pajaro.hablar() #hola soy un pajaro y mi nombre es Polly

#%%
# Composition of classes
class Categorias:
    nombreCategoria = ''

class Proveedor:
    nombreProveedor = ''

class Producto:
    idproducto = 0
    CategoriaProducto = Categorias()
    precio = 0
    tamaño = 0
    CIFProveedor = Proveedor()

p = Producto()
p.CategoriaProducto.nombreCategoria = 'Electronicos'
p.CIFProveedor.nombreProveedor = 'Electronicos'


#%%
class Juguete:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    
    # str y repr son funciones que se ejecutan cuando se imprime un objeto
    def __str__(self): #salidas informales
        return f"{self.nombre} es un {self.tipo}"
    def __repr__(self): #salidas tecnicas
        return f"Juguete('{self.nombre}', '{self.tipo}')"

j1 = Juguete('Pelota', 'bebe')
print(str(j1)) #Pelota es un bebe
print(repr(j1)) #Juguete('Pelota', 'bebe')






"""----------------------------- MAP/FILTER/REDUCE -----------------------------"""
#%%
# Filter : se aplica el filtro cuando la condicion es verdadera (True)
numero = [1,2,3,4,5,6,7,8,9,10]
def esPar(numero): #Se ejeucta para cada elemento de la lista
    return numero % 2 == 0
#filter
filtro = list(filter(esPar, numero))
print(type(filtro)) #<class 'list'>
print(f'Filtro: {filtro}') #Filtro: [2, 4, 6, 8, 10]
# lambda
filtro = list(filter(lambda numero: numero % 2 == 0, numero))
print(f'Filtro lambda: {filtro}') #Filtro lambda: [2, 4, 6, 8, 10]


#%%
# Map : se aplica sobre cada elemento de la lista
numero = [1,2,3,4,5,6,7,8,9,10]
def doble(numero): #funcion anonima, se ejecuta sobre cada elemento de la lista
    print('doble:', numero * 2)
    return numero * 2
#map
doble = list(map(doble, numero))
print(type(doble)) #<class 'list'>
print(f'Map: {doble}') #Map: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
# lambda
doble = list(map(lambda x : x * 2, numero))
print(f'Map lambda: {doble}') #Map lambda: [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]



#%%
# Reduce : itera sobre la lista y aplica una funcion a cada elemento
from functools import reduce
numero = [1,2,3,4,5,6,7,8,9,10]
def suma(numero1, numero2): # se ejecuta como un for
    print (f'{numero1} + {numero2} = {numero1 + numero2}')
    return numero1 + numero2
#reduce
suma = reduce(suma, numero)
print(type(suma)) #<class 'int'>
print(f'Reduce: {suma}') #Reduce: 55
# lambda
suma = reduce(lambda numero1, numero2 : numero1 + numero2, numero)
print(f'Reduce lambda: {suma}') #Reduce lambda: 55











