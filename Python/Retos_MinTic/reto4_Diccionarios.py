#%%
diccionario_entrada = input()
#Convertir diccionario string a diccionario
diccionario_entrada = eval(diccionario_entrada)
laminas_deseadas = input().split()
precio=0
laminas_encontradas=""


for key in laminas_deseadas:
    if key in diccionario_entrada:
        precio += diccionario_entrada[key]
        laminas_encontradas += key + " "
        
print(precio)
print(laminas_encontradas)