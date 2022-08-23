#%%
#Programa que recibe una lista de caracteres separada por coma
lista = list(input().split(","))
cont = 1
#Toda la lista en mayusculas
lista = [x.upper() for x in lista]
listab= []
repetidos=""
#contar las letras consecutivas
for i in range(len(lista)):
    if i!=(len(lista)-1):
        if lista[i]==lista[i+1]:
            cont+=1
        else:
            listab.append(lista[i])
            repetidos=repetidos+str(cont)
            cont=1
    else:
        listab.append(lista[i])
        repetidos=repetidos+str(cont)
print(*[x for x in listab])
print(*[x for x in repetidos])