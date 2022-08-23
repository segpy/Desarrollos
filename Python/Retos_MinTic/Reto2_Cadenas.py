#%%
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


# %%
