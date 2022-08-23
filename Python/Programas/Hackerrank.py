#%% DATE & TIME 
"""
Multiple input.
Imprimir el dia en mayuscula a partir de una fecha dada
"""
import calendar

m,d,y = map(int,input().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())

#%% DATE & TIME
"""
Convierte un String a tipo datatime.
Obtiene la diferencia en segundos a partir de a y b fechas dadas.
Se debe mantener el formato del string de entrada, formato de entrada -> fmt
Input:
2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
"""
from datetime import datetime as dt
n = int(input())
format = "%a %d %b %Y %H:%M:%S %z"
for i in range(n):
    fecha_1 = input()
    fecha_2 = input()
    #Imprime las fechas en formato datetime
    print(dt.strftime(dt.strptime(fecha_1,format), format))
    print(dt.strftime(dt.strptime(fecha_2,format), format))
    #Restar las fechas en segundos usando el modulo datetime
    print(abs(int((dt.strptime(fecha_1,format) - dt.strptime(fecha_2,format)).total_seconds())))
    


#%% LIST NESTED (LISTA ANIDADA)

#METODO 1. Input con List comprenhension
n = int(input('Cantidad'))
marksheet = [[input('Nombre: '), float(input('Nota: '))] for i in range(n)]
print(marksheet,'Antes')
marksheet.sort()
print(marksheet,'Despues')
b=[]
#print(b = [i for i in marksheet if i[0] != marksheet[0][0]])
for i in marksheet:
    print('i[0] iteracion:',i[0])
    if i[0] != marksheet[0][0]:
        print('i[0] :',i[0][0])
        print('mark[0][0] :',marksheet[0][0])
        b.append(i)
print('b de for: ',b)
b = [i for i in marksheet if i[0] != marksheet[0][0]]
print('b de comprension: ',b)
c = [j for j in b if j[0] == b[0][0]]
c.sort(key=lambda x: x[1])
for i in range(len(c)):
    print(c[i][1])
        
#METODO 2. Input con for anidados.
"""
lista_grande = []
for i in range(0,4):
    lista_pequeña=[]
    for j in range(0,i+1):
        lista_pequeña.append(input(f'Ingrese el valor:  {i} , {j}:\n'))
    lista_grande.append(lista_pequeña)
print(lista_grande)
"""
#%% LIST COMPRENHENSION
"""
Multiple input con for.
Llenado de lista elegante
Uso de corchete "[]" para mantener el tipo lista.
Uso de parentesis "()" para cambiar a tipo generador
"""
x,y,z,n = (int(input()) for i in range (4))
b=1
c=2
lista1=[[a,b,c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a+b+c!=n]
print(lista1)

#%% LIST COMPRENHENSION
"""
Multiple input como lista
Uso de list comprenhension
"""
n = int(input())
arr = list(map(int, input().split()))
print([x for x in arr])
print(max([x for x in arr if x<max(arr)]))

#%% RANDOM LIST
import random
list_a=[]
list_a1=[]
list_b=[]
list1=['nombre1','nombre2','nombre3','nombre4','nombre5','nombre6','nombre7','nombre8','nombre9','nombre10','nombre11','nombre12']
list_a=(random.sample(list1,6))
#print('sin sortear:',list_a)
list_a.sort()
#print('sorteado:',list_a)

#Recorre los items de la lista y guarda segun las condiciones
for i in list1:
    if i not in list_a:
        list_b.append(i)
    else:
        list_a1.append(i)
print(f'Grupo 1: \n{list_a1}')
print(f'Grupo 2: \n{list_b}')
"""
list_bprueba=(random.sample(list1,6))
list_b=[b for b in list1 if b!=list_a]
"""
#%% PRINT()

n=int(input())
#metodo 1
print('Metodo 1:\n',*range(1,n+1),sep='')
#metodo 2
for i in range(1,n+1):
        print(i,end="")



