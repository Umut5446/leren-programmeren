# vraag console of pc
# vraag of iemand member is. 15 euro korting indien console
# bereken prijs pc 45 Euro
# consoles 55 Euro

from challenge import Verschil_prijs
from smartphone import Iphone_13_prijs


CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15

platform = input('Ben je pc of console gamer?')
prijs = PC_PRIJS 

if platform == 'console': 
    prijs = CONSOLE_PRIJS
if input('Bent u member?') == 'Ja':
    prijs = MEMBER_KORTING
else:
        prijs = PC_PRIJS
print(f'U bent {platform} gamer, dan kost de game: {prijs} Euro')

KORTINGS_PRIJS = CONSOLE_PRIJS / 100 * MEMBER_KORTING
totaal_prijs = CONSOLE_PRIJS - KORTINGS_PRIJS

print(f'Met {MEMBER_KORTING} procent korting kost het met member {totaal_prijs}')


naam = input(f'Hoe heet je?')
#########################################################################################
 

prijs_iphone = int(input('Hoe duur is de iphone?'))
prijs_galaxy = int(input('Hoe duur is de galaxy'))

print(prijs_iphone)
print(prijs_galaxy)

if prijs_iphone > prijs_galaxy:
    duurste_telefoon =  IPHONE
    goedkoopste_telefoon = GALAXY
    prijs_duurste = prijs_iphone
    prijs_goedkoopste = prijs_galaxy
else: 
    duurste_telefoon = GALAXY
    goedkoopste_telefoon = IPHONE
    prijs_duurste = prijs_galaxy
    prijs_goedkoopste = prijs_iphone

print(f'De {duurste_telefoon} is het duurst, de telefoon kost: {prijs_duurste} Euro')
print(f'De {goedkoopste_telefoon} is het goedkoopst, de telefoon kost: {prijs_goedkoopste} Euro')

Verschil_prijs = prijs_iphone - prijs_galaxy
if Verschil_prijs > 50: 
    advies_telefoon = GALAXY
else:
        advies_telefoon = IPHONE

print(f'Het advies is dus de {advies_telefoon} te kopen. Verschil: {Verschil_prijs}.')
############################################################################################################
Duur = input('Is de kaas duur?')
if Duur == 'Ja':
    Duur = input('Zit er een korst om?')
    if Duur == 'Ja':
        print('De kaas die jij bedoelt is de Emmenthaler.')
    else:
        print('De kaas die jij bedoelt is Gouda.')
elif Duur ==    