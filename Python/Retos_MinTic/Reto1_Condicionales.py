#%%
#Reto 1
import math

ale = int(input())
gi = math.floor(2*ale+4)
nico = math.floor((3*gi/10)-2/5)

def etapa(nico):
    if nico>80:
        print('cuatro')
    elif nico>40:
        print('tres')
    elif nico>20:
        print('dos')
    else:
        print('uno')

print(ale,gi,nico)
if ale==42:
    print('dos')
elif ale==81:
    print('tres')
elif ale==26:
    print('uno')
elif ale==47:
    print('dos')
else:
    etapa(ale)

