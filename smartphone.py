from re import I


Iphone_13_prijs = 700
Samsung_Galaxy_S22_prijs = 600

Iphone_13_prijs = float(input(f'Hoe duur is de Iphone?'))
Samsung_Galaxy_S22_prijs = float(input(f'hoe duur is de Samsung Galaxy S22?'))

print(f'De Iphone is het duurst, de telefoon kost: {Iphone_13_prijs}')
Iphone_13_prijs = round(Iphone_13_prijs,2)

print(f'De Samsung Galaxy S22 is het goedkoopst de telefoon kost: {Samsung_Galaxy_S22_prijs}')

Prijs_verschil = Iphone_13_prijs - Samsung_Galaxy_S22_prijs

print(f'Het advies is dus de Samsung Galaxy S22 te kopen. Deze is namelijk {Prijs_verschil} euro goedkoper dan de Iphone.')
