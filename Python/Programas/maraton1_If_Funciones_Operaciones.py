""" PROBLEMAS DE CONDICIONALES"""
#%%
#Dadas tres longitudes positivas, determinar si con esas longitudes se puede construir un triangulo
lado1,lado2,lado3 = (int(input('Ingrese el lado '))for i in range(3))

def tipo_triangulo(a,b,c):
    if a==b and a==c:
        print('Equilatero')
    elif a!=b and a!=c:
        print('Escaleno')
    else:
        print('Isosceles')

tipo_triangulo(lado1,lado2,lado3)
#%%
#Dado el centro y el radio de un cırculo, determinar si un punto de R2 pertenece o no al interior del cırculo.

centro,radio = list(map(int, input('Ingrese el centro: ').split())),int(input('Ingrese el radio: '))
puntos = list(map(int, input('Ingrese los puntos: ').split()))
x = puntos[0]
y = puntos[1]
def circulo (centro,radio,x,y):
    if radio**2 >= (x-centro[0])**2 + (y-centro[1])**2:
        print('Punto dentro del circulo')
    else:
        print('Punto fuera del circulo')
circulo(centro,radio,x,y)

# %%
# Dados dos numeros reales distintos de cero (0), x y y que representen
# la abscisa y ordenada de un punto (x, y) ∈ R2, determinar a que cuadrante 
# del plano cartesiano pertenece el par ordenado.
x,y = int(input('Ingrese x: ')),int(input('Ingrese y: '))

def cuadrante(x,y):
    if x>0 and y>0:
        print('1')
    elif x<0 and y>0:
        print('2')
    elif x<0 and y<0:
        print('3')
    else:
        print('4')

cuadrante(x,y)

# %%  Dado un numero real x, construya una funcion que permita
# determinar si el numero es positivo, negativo o cero. Para cada caso
# de debe imprimir el texto que se especifica a continuacion:
#Positivo: “El numero x es positivo”
# Negativo: “El numero x es negativo”
# Cero (0): “El numero x es el neutro para la suma”

x = int(input('Ingrese x: '))

def numero(x):
    if x>0:
        print('Positivo')
    elif x<0:
        print('Negativo')
    else:
        print('Cero')
numero(x)

#%%
#Dado un caracter, construya un programa en Python para determinar si el caracter es un dıgito o no.

caracter = input('Ingrese el caracter: ')

def digitoono(valor):
    if valor.isdigit():
        print('Es un digito')
    else:
        print('No es un digito')
digitoono(caracter)

#%%
#Dada una cadena de longitud 1, determine si el codigo ASCII de 
# primera letra de la cadena es par o no. Ayuda: utilice la funcion 
# ord(<caracter>) de Python que retorna el codigo ASCII de una cadena de longitud 1.

caracter = input('Ingrese el caracter: ')

def asscii(caracter):
    if ord(caracter)%2 == 0:
        #print('Caracter',ord(caracter))
        print('Es par')
    else:
        print('Es impar')
asscii(caracter)

#%%
#Dado un numero entero, determinar si ese numero corresponde al
# codigo ASCII de una vocal minuscula. Ayuda: utilice la funcion
# chr(<numero>) de Python que retorna el caracter ASCII
# correspondiente al numero entero en el cual se evalue la funcion

numero = int(input('Ingrese el numero: '))
# Funcion que determina si es vocal minuscula
def funcion_1(valor):
    if chr(valor) in 'aeiou':
        print('Es vocal')
    else:
        print('No es vocal')
funcion_1(numero)

#%%

""" PROBLEMAS DE FUNCIONES"""
#%% 
#El numero de contagiados de Covid-19 en el paıs de NuncaLandia se duplica cada dıa.
#Hacer un programa que diga el numero total de 
# personas que se han contagiado cuando pasen D dıas a partir de hoy,
# si el numero de contagiados actuales es C

c = int(input('Ingrese el numero de contagiados actuales: '))
d = int(input('Ingrese los dias: '))
def contagiados(c,d):
    if d>0:
        print(c*2*d)
    else:
        print('El numero de contagiados es: ',c)
contagiados(c,d)

#%%
#Si pido prestados P cantidad de pesos para pagarlos en dos meses, si
# el interes del prestamo es del 3% al mes. ¿Cuanto se debe pagar al
# final del segundo mes si el interes es compuesto mensualmente?

p = int(input('Ingrese el numero de pesos: '))
def prestamo(p):
    if p>0:
        print(p*1.03**2)
    else:
        print('El numero de pesos es: ',p)
prestamo(p)

#%%
#Mi mama me manda a comprar P panes a $ 300 cada uno, M bolsas
# de leche a $ 3300 cada una y H huevos a $ 350 cada uno. Hacer un
# programa que me diga las vueltas (o lo que quedo debiendo) cuando
# me da un billete de B pesos

billete = int(input('Ingrese el numero de pesos: '))
panes = int(input('Ingrese el numero de panes: '))
leche = int(input('Ingrese el numero de leche: '))
huevos = int(input('Ingrese el numero de huevos: '))
def compras(billete,leche,huevos,panes):
    if billete>0:
        print(billete-300*panes-3300*leche-350*huevos)
    else:
        print('El numero de pesos es: ',billete)
compras(billete,leche,huevos,panes)

#%%
#Diseñe una funcion que calcule la cantidad de carne de aves en kilos
# si se tienen N gallinas, M gallos y K pollitos cada uno pesando 6
# kilos, 7 kilos y 1 kilo respectivamente
n = int(input('Ingrese el numero de gallinas: '))
m = int(input('Ingrese el numero de gallos: '))
k = int(input('Ingrese el numero de pollitos: '))
def cantidad(n,m,k):
    if n>0 and m>0 and k>0:
        print(n*6+m*7+k)
    else:
        print('Ingrese un numero mayor a 0')
cantidad(n,m,k)

#%%
""" VOLUMEN DE SOLIDOS"""
#Importar libreria math
import math
#Volumen de una esfera = 4/3 * pi * r^3
#Volumen de un cono = pi * r^2 * h / 3

r1 = float(input('Ingrese el radio de la esfera: '))
r2 = float(input('Ingrese el radio del cono: '))
h = float(input('Ingrese la altura del cono: '))
#Volumen usando variable pi
def volumen(r1,r2,h):
    if r1>0 and r2>0 and h>0:
        print(round(4/3*math.pi*r1**3,2))
        print(round(math.pi*r2**2*h/3,2))
    else:
        print('Ingrese un numero mayor a 0')
volumen(r1,r2,h)

#Para r1=3 h=4.5 y r2=4, Volumen_esfera = 113.09 Volumen_cono = 75.39
#Para r1=3 h=4 y r2=4, Volumen_esfera = 113.09 Volumen_cono = 67.02
#%%
#Area de un rectangulo = base * altura
#Area de un circulo = pi * r^2

base = float(input('Ingrese la base del rectangulo: '))
altura = float(input('Ingrese la altura del rectangulo: '))
radio = float(input('Ingrese el radio del circulo: '))
#Area usando variable pi
def area(base,altura,radio):
    if base>0 and altura>0 and radio>0:
        print(round(base*altura+(math.pi*radio**2)*2,2))
    else:
        print('Ingrese un numero mayor a 0')
area(base,altura,radio)

#%%
#Area lateral v2

base1 = float(input('Ingrese la base del rectangulo 1: '))
altura1 = float(input('Ingrese la altura del rectangulo 1: '))
base2 = float(input('Ingrese la base del rectangulo 2: '))
altura2 = float(input('Ingrese la altura del rectangulo 2: '))
radio1 = float(input('Ingrese el radio del circulo 1: '))
radio2 = float(input('Ingrese el radio del circulo 2: '))

#Area usando variable pi
def area_lateral(base1,altura1,base2,altura2,radio1,radio2):
    if base1>0 and altura1>0 and base2>0 and altura2>0 and radio1>0 and radio2>0:
        print(round(base1*altura1+base2*altura2+(math.pi*radio1**2)+(math.pi*radio2**2),2))
    else:
        print('Ingrese un numero mayor a 0')

def area_circulo(radio1):
    if radio1>0:
        return round(math.pi*radio1**2,2)
    else:
        print('Ingrese un numero mayor a 0')
def area_rectangulo(base1,altura1):
    if base1>0 and altura1>0:
        return round(base1*altura1,2)
    else:
        print('Ingrese un numero mayor a 0')
#Funcion que implementa las funciones area circulo y area rectangulo
def area_lateral_v2(base1,altura1,base2,altura2,radio1,radio2):
    if base1>0 and altura1>0 and base2>0 and altura2>0 and radio1>0 and radio2>0:
        print(round(area_rectangulo(base1,altura1)+area_rectangulo(base2,altura2)+area_circulo(radio1)+area_circulo(radio2),2))
    else:
        print('Ingrese un numero mayor a 0')

area_lateral(base1,altura1,base2,altura2,radio1,radio2)
area_lateral_v2(base1,altura1,base2,altura2,radio1,radio2)

""" PROBLEMAS DE EVALUACION DE EXPRESIONES"""
#%%
#Si en la UN estan podando arboles y cada rama tiene P hojas, y a
# cada arbol le quitaron K ramas, cuantos arboles se deben podar para
# obtener T hojas?.

Phojas = int(input('Ingrese el numero de hojas por rama: '))
Kramas = int(input('Ingrese el numero de ramas por arbol: '))
hojas_totales = int(input('Ingrese el numero de hojas deseadas: '))

def arboles(Phojas,Kramas,hojas_totales):
    if Phojas>0 and Kramas>0 and hojas_totales>0:
        print(hojas_totales//(Phojas*Kramas))
    else:
        print('Ingrese un numero mayor a 0')
arboles(Phojas,Kramas,hojas_totales)
#%%
#Si un amigo, no tan amigo, me presta K pesos a i pesos de interes
# diario, ¿cuanto le pagare en una semana si el interes es simple?, ¿y
# cuanto si el interes es compuesto?.

prestamo = int(input('Ingrese el monto del prestamo: '))
interes_diario = float(input('Ingrese el interes diario en pesos: '))
interes_porcentaje = interes_diario/prestamo

def interes(prestamo,inte):
    if prestamo>0 and inte>0:
        print(round(prestamo*(1+inte*7),2))
        print(round(prestamo*(1+inte)**7,2))
    else:
        print('Ingrese un numero mayor a 0')
interes(prestamo,interes_porcentaje)

#%%
#En una granja se crıan un numero de V - Vacas, A - Aves (pollos y 
# gallinas) y E - escorpiones. Las vacas estan encerradas en un corral de
# N × M metros cuadrados, las aves en un galpon y los escorpiones en
# vitrinas. Para cada subproblema utilice solo los datos que necesite

#Si una vaca necesita K metros cuadrados de pasto para producir X 
# litros de leche por dıa, ¿cuantos litros de leche se producen por
# semana en la granja?.
vacas = int(input('Ingrese el numero de vacas: '))
aves = int(input('Ingrese el numero de aves: '))
escorpiones = int(input('Ingrese el numero de escorpiones: '))
n,m = (int(x) for x in input('Ingrese el numero de metros cuadrados del corral: ').split())
pasto = int(input('Ingrese el numero de metros cuadrados del pasto que requiere una vaca: '))
litros_dia = int(input('Ingrese los litros de leche producidos por una vaca al dia: '))

corral = n*m
def leche(corral,pasto,litros,vacas):
    if corral>0 and pasto>0 and litros>0:
        print(round(((corral//pasto)*litros)*vacas,2))
    else:
        print('Ingrese un numero mayor a 0')
leche(corral,pasto,litros_dia,vacas)

# Si 1/3 de las aves que hay en la granja son gallinas, y la mitad de las
# gallinas ponen 1 huevo cada 3 dıas y la otra mitad 1 huevo cada 5
# dıas, ¿en un mes cuantos huevos producen? (1 mes ≡ 30 dıas).

gallinas = aves//3
huevos_gallinas = 1/2*gallinas
def huevos(gallinas,huevos_gallinas):
    if gallinas>0 and huevos_gallinas>0:
        print(round(huevos_gallinas*30/3+huevos_gallinas*30/5,2))
    else:
        print('Ingrese un numero mayor a 0')
huevos(gallinas,huevos_gallinas)

#Si los escorpiones de la granja se venden a China, y hay escorpiones
# de tres diferentes tamaños: pequeños (con un peso de 20 gramos),
# medianos (con un peso 30 gramos) y grandes (con un peso de 50
# gramos), ¿cuantos kilos de escorpiones se pueden vender sin que
# decrezca la poblacion a menos de 2/3?.
#%%
#Al granjero se le daño el corral y no sabe si volver a cercar el corral
# con madera, alambre de puas o poner reja de metal. Si va a cercar
# con madera debe poner 4 hileras de tablas, con varilla 8 hileras y con
# alambre solo 5 hileras, el quiere saber que es lo menos costoso para
# cercar si sabe que el alambre de puas vale P por metro, las tablas a Q
# por metro y las varillas S por metro. Dado el tamaño del corral y los
# precios de los elementos, ¿cual cerramiento es el mas economico?.

P_alambre = int(input('Ingrese el precio del alambre por metro: '))
Q_tablas = int(input('Ingrese el precio de las tablas por metro: '))
S_varillas = int(input('Ingrese el precio de las varillas por metro: '))

def barato(P,Q,S):
    if P>0 and Q>0 and S>0:
        #Condicion para escoger el mas economico entre P,Q,S
        if P*5<Q*4 and P*5<S*8:
            print('El mas barato es alambre')
        elif Q*4<P*5 and Q*4<S*8:
            print('El mas barato es tablas')
        else:
            print('El mas barato es varillas')

    else:
        print('Ingrese un numero mayor a 0')
barato(P_alambre,Q_tablas,S_varillas)
#%%
"""
#Realizar un programa que me diga cuanto debo pagar al cabo de 3 meses con un interes compuesto efectivo anual del 20% si me prestan una cantidad de $400.000
#Pasar de interes efectivo anual a efectivo mensual
interes_efectivo_mensual = (1+0.2)**(1/12)-1
meses = 3
cantidad_prestamo = 400000

#Funcion que calcula el interes simple
def interes_simple(cantidad_prestamo,interes_efectivo_mensual,meses):
    if cantidad_prestamo>0 and interes_efectivo_mensual>0 and meses>0:
        print(round(cantidad_prestamo*(1+interes_efectivo_mensual*meses),2))
    else:
        print('Ingrese un numero mayor a 0')
interes_simple(cantidad_prestamo,interes_efectivo_mensual,meses)

#Funcion que calcula el interes compuesto
def interes_compuesto(cantidad_prestamo,interes_mensual,meses):
    if cantidad_prestamo>0 and interes_mensual>0 and meses>0:
        print(round(cantidad_prestamo*(1+interes_mensual)**meses,2))
    else:
        print('Ingrese un numero mayor a 0')

interes_compuesto(cantidad_prestamo,interes_efectivo_mensual,meses)

#%%
#Cada rollo de papel tiene 100 hojas, y se usa a diario 20 hojas de papel, cuantos rollos de papel se necesitan comprar al mes para cubrir el consumo de papel de una persona al mes?
rollo_papel = 100
hojas_papel = 20
dias = 30
personas = int(input('Ingrese el numero de personas: '))
#Cantidad de rollos de papel que se necesitan comprar al mes
rollo_papel_mes =hojas_papel*dias/rollo_papel
print(round(rollo_papel_mes*personas,2))

#%%
"""

