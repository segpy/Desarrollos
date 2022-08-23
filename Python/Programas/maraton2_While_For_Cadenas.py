"""Problemas de ciclo mientras/for."""
#%%
#Desarrollar un programa que imprima el cuadrado del numero que el
# usuario ingresa mientras que el numero ingresado no sea negativo.
i=0
while i==0:
    numero = int(input("Ingrese un numero: "))
    if numero > 0:
        print(numero**2)
    

#%%
#Desarrollar un programa que dado un numero entero positivo n
#calcule e imprima (separados por espacios) n/2 si es par o 3n + 1 si es
# impar. El programa debe repetir el proceso con el numero resultado
# de dicha operacion mientras este sea diferente de 1. Por ejemplo para
# el n umero 3 debe imprimir 10 5 16 8 4 2 1
i=0

while i==0:
    numero = int(input("Ingrese un numero: "))
    while numero!=1:
        if numero % 2 == 0:
            print(numero/2)
            numero = numero/2
        else:
            print(3*numero + 1)
            numero = 3*numero + 1

#%%
#En 2022 el paıs A tendra una poblacion de 25 millones de habitantes
# y el paıs B de 18.9 millones. Las tasas de crecimiento anual de la
# poblacion seran de 2% y 3% respectivamente. Desarrollar un
# programa que imprima el año en que la poblacion del paıs B superara
# a la de A
poblacion_A = 25000000
poblacion_B = 18900000
tasa_a = 0.02
tasa_b = 0.03
for años in range(1,100):
    poblacion_A = poblacion_A + (poblacion_A*tasa_a)
    print(poblacion_A)
    poblacion_B = poblacion_B + (poblacion_B*tasa_b)
    print(poblacion_B)
    if poblacion_B > poblacion_A:
        print(f'El pais B supera a A en {años} años')
        break

#%%
#Diseñar una funcion que permita calcular el  ́epsilon de la maquina. El
#  ́epsilon de maquina es el numero decimal mas pequeño que sumado
# a 1 se puede representar de manera precisa en la maquina (que no es
# redondeado), es decir, retorna un valor diferente de 1,  ́este da una idea
# de la precision o numero de cifras reales que pueden ser almacenadas
# en la maquina. La idea es realizar un ciclo en el cual se realiza la
# operacion 1 +  para potencias de 2 desde  = 2^0 y continuando con
# potencias decrecientes de 2 ( = 2^(−1), = 2^(−2), = 2^(−3), = 2^(−4),...)
# hasta obtener que el resultado de la suma 1 +  no se altere

for i in range(0,-1000,-1):
    anterior_operacion = operacion
    print(anterior_operacion)
    print(operacion)
    operacion = 1+2**i
    #Comprobar si operacion no se altera
    if anterior_operacion == operacion:
        print(f'El epsilon de la maquina es {operacion}')
        print(f'Iteraciones: {i}')
        break

"""Problemas de ciclo para/for."""
#%%
#Imprimir un listado con los n ́umeros del 1 al 100 cada uno con su
# respectivo cuadrado.
print("Listado de numeros del 1 al 100 con su cuadrado")
print(*[(i,i**2) for i in range(1,101)])
#%%
#Imprimir un listado con los numeros impares desde 1 hasta 999 y
# seguidamente otro listado con los numeros pares desde 2 hasta 1000
print("Listado de numeros impares desde 1 hasta 999")
print(*[i for i in range(1,1000,2)])
print("Listado de numeros pares desde 2 hasta 1000")
print(*[i for i in range(2,1001,2)])
#%%
#Imprimir los numeros pares en forma descendente hasta 2 que son
# menores o iguales a un numero natural n ≥2 dado
numero = int(input("Ingrese un numero: "))
print(*[i for i in range(numero,1,-1) if i%2==0])
#%%
#Imprimir los numeros de 1 hasta un numero natural n dado, cada uno
# con su respectivo factorial.
import math
numero = int(input("Ingrese un numero: "))
#Obtener el factorial de un numero
def factorial(numero):
    if numero == 0:
        return 1
    else:
        return numero * factorial(numero-1)
print(*[(i,factorial(i)) for i in range(1,numero+1)])
print(*[(i,math.factorial(i)) for i in range(1,numero+1)])
#%%
#Calcular el valor de 2 elevado a la potencia n
numero = int(input("Ingrese un numero: "))
print(2**numero)

#%%
#Leer un numero natural n, leer otro dato de tipo real x y calcular x^n
# y mostrar el resultado
numero = int(input("Ingrese un numero: "))
x = float(input("Ingrese un numero: "))
print(x**numero)
#%%
# Disene un programa que muestre las tablas de multiplicar del 1 al 9. 
print("Tabla de multiplicar del 1 al 9")
for tabla in range(1,10):
    print(f"Tabla del {tabla}")
    print(*[tabla*numero for numero in range(1,10)]) 
#%%
#Diseñar una funcion que permita calcular una aproximacion de la
# funcion exponencial alrededor de 0 para cualquier valor x∈R,
# utilizando los primeros n terminos de la serie de Maclaurin
import math

numero = int(input("Ingrese un numero: "))
x = float(input("Ingrese un numero real: "))
exponencial = 0
for i in range(0,numero+1):
    exponencial+=x**i/math.factorial(i)
print(exponencial)
print(math.exp(x))


#%%
#imprimir primeros n numeros de la serie de taylor
# de la funcion seno
import math

n = int(input("Ingrese un numero: "))
x = float(input("Ingrese un numero real: "))
seno= 0

for i in range(0,n+1):
    #implementar la funcion seno aproximada
    seno+=(-1)**i*x**(2*i+1)/math.factorial(2*i+1)
print(seno)
print(math.sin(x))

#%%
#Programa que calcula el valor de la funcion coseno aproximada 
# para cualquier valor x∈R y muestra el resultado
import math
n = int(input("Ingrese un numero: "))
x = float(input("Ingrese un numero real: "))
coseno =0
for i in range(0,n+1):
    coseno+=(-1)**i*x**(2*i)/math.factorial(2*i)
print(coseno)
print(math.cos(x))

#%%
#Programa que calcula el valor de la funcion logaritmo natural aproximada
# para cualquier valor x∈R y muestra el resultado
import math
n = int(input("Ingrese un numero: "))
x = float(input("Ingrese un numero real: "))
logaritmo = 0
for i in range(0,n+1):
    logaritmo+=(1/(2*i+1))*(x**2-1/(x**2+1))**(2*i+1)
print(logaritmo)
#Logaritmo natural con funcion math
print(math.log(x))

#%%
#Programa que calcula el valor de la funcion arcotangente aproximada
# para cualquier valor x entre 1 y -1 y muestra el resultado
import math
n = int(input("Ingrese un numero: "))
x = float(input("Ingrese un numero real: "))
arcotangente = 0
#intenta si x esta entre 1 y -1
while x<1 and x>-1:
    for i in range(0,n+1):
        arcotangente+=(-1)**i*x**(2*i+1)/(2*i+1)
    print(arcotangente)
    print(math.atan(x))
    break

""" Problemas de cadenas"""
#%%
#Desarrollar un algoritmo que reciba dos cadenas de caracteres y
# determine si la primera esta incluida en la segunda. Se dice que una
# cadena esta incluida en otra, si todos los caracteres (con repeticiones)
# de la cadena esta en la segunda cadena sin tener en cuenta el orden
# de los caracteres
cadena1= input("Ingrese una cadena: ")
cadena2= input("Ingrese una cadena: ")
#seleccionar las letras que no se repiten de la cadena1
letras = set(cadena1)
no_estan= ''
for caracter in letras:
    #metodo count
    if cadena2.count(caracter)<cadena1.count(caracter):
        no_estan+=(caracter+',')
    
#verificar si la variable no_estan esta vacia
if no_estan=='':
    print(f'{cadena1} esta incluida en {cadena2}')
else:
    print(f'Las cadenas no son iguales, las letras ({no_estan}) no estan en la segunda cadena')

#%%
#Desarrollar un algoritmo que invierta una cadena de caracteres.
cadena1 = input("Ingrese una cadena: ")
print('Cadena original: ',cadena1)
#invertir la cadena
print('Cadena invertida: ',cadena1[::-1])

#%%
#Desarrollar un algoritmo que determine si una cadena de caracteres es
# palındrome. Una cadena se dice pal ́ındrome si al invertirla es igual a
# ella misma
cadena1 = input("Ingrese una cadena: ")
#invertir la cadena
cadena2 = cadena1[::-1]
for i in range(0,len(cadena1)):
    if cadena1[i]!=cadena2[len(cadena1)-i-1]:
        palindrome = False
        #print(f'{cadena1} no es palindrome')
        #print(cadena1[i],cadena2[len(cadena1)-i-1])
        break
    else:
        palindrome = True
        #print(f'{cadena1} es palindrome')
if palindrome:
    print(f'{cadena1} es palindrome con {cadena2}')
else:
    print(f'{cadena1} no es palindrome')
#%%
import re
#Desarrollar un algoritmo que determina si una cadena de caracteres es
# frase palındrome, esto es, si es palındrome al eliminarle espacios,
# tıldes, signos de puntuacion y al considerar mayusculas=minusculas
cadena1 = input("Ingrese una cadena: ")
cadena1_original = cadena1
cadena2_original = cadena1[::-1]
#eliminar espacios
cadena1 = cadena1.replace(' ','')
#eliminar tildes con metodo maketrans
cadena1 = cadena1.translate(str.maketrans('áéíóú','aeiou'))
#eliminar signos de puntuacion con modulo re
cadena1 = re.sub(r'[^\w\s]','',cadena1)
#toda la cadena1 en minusculas
cadena1 = cadena1.lower()
#invertir la cadena
cadena2 = cadena1[::-1]
for i in range(0,len(cadena1)):
    if cadena1[i]!=cadena2[len(cadena1)-i-1]:
        palindrome = False
        #print(f'{cadena1} no es palindrome')
        #print(cadena1[i],cadena2[len(cadena1)-i-1])
        break
    else:
        palindrome = True
        #print(f'{cadena1} es palindrome')
if palindrome:
    print(f'{cadena1_original} es palindrome con {cadena2_original}')
else:
    print(f'{cadena1_original} no es palindrome')










