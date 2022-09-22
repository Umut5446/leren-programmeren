Iphone_13_prijs = 900
Samsung_Galaxy_S22_prijs = 850
Asus_Zenfone_9 = 800

float(input(f'Hoe duur is de iphone 13?'))
float(input(f'Hoe duur is de Samsung Galaxy S22?'))
float(input(f'Hoe duur is de Asus Zenfone 9?'))

print(f'De Iphone 13 is het duurst, de telefoon kost: {Iphone_13_prijs}')
print(f'De Asus Zenfone 9 is het goedkoopst, de telefoon kost: {Asus_Zenfone_9}')
print(f'De Samsung Galaxy S22 zit er tussenin met: {Samsung_Galaxy_S22_prijs}')


Verschil_prijs = Iphone_13_prijs - Samsung_Galaxy_S22_prijs
Verschilprijs= Iphone_13_prijs - Asus_Zenfone_9
print(f'Het advies is dus de Asus Zenfone 9 te kopen. Deze is namelijk {Verschilprijs} goedkoper dan de Iphone 13 en {Verschil_prijs} goedkoper dan de Samsung Galaxy S22.')