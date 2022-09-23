
from ast import AnnAssign


Iphone_13_prijs = int(input(f'Hoe duur is de Iphone?'))
Samsung_Galaxy_S22_prijs = int(input(f'hoe duur is de Samsung Galaxy S22?'))

Prijs_verschil = Iphone_13_prijs - Samsung_Galaxy_S22_prijs

if Prijs_verschil > 50:
    advies = 'galaxy'
    niet = 'iphone'
    aankoop_prijs = Samsung_Galaxy_S22_prijs
    niet_prijs = Iphone_13_prijs
else:
    advies = 'iphone'
    niet = 'galaxy'
    aankoop_prijs = Iphone_13_prijs
    niet_prijs = Samsung_Galaxy_S22_prijs

if aankoop_prijs - niet_prijs > 0:
   goedkoper_duurder = 'duurder'

else:
    goedkoper_duurder = 'goedkoper'

print(f'Het advies is dus de {advies} te kopen. Deze is namelijk {aankoop_prijs}')



