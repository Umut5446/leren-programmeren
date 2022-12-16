from ast import While
from pickle import TRUE


Pizza_small_prijs = 4.99
Pizza_medium_prijs = 7.99
Pizza_large_prijs = 9.99

Pizza_small_prijs = float(input(f'Hoeveel kost het pizza small per stuk?'))
Pizza_small_aantal = int(input(f'Hoeveel pizzas wilt u?'))

while True:
    try:
            Pizza_small_aantal = int(input("Hoeveel pizza's wilt u hebben?"))
            break
    except: ValueError
    print(f'Je moet wel een getal invullen')

Pizza_medium_prijs = float(input(f'Hoeveel kost het pizza medium per stuk?'))
Pizza_medium_aantal = int(input(f'Hoeveel pizzas wilt u?'))

while True:
    try:
            Pizza_medium_aantal = int(input("Hoeveel pizza's wilt u hebben?"))
            break
    except: ValueError
    print(f'Je moet wel een getal invullen')


Pizza_large_prijs = float(input(f'Hoeveel kost het pizza large per stuk?'))
Pizza_large_aantal = int(input(f'Hoeveel pizzas wilt u?'))

while True:
    try:
            Pizza_large_aantal = int(input("Hoeveel pizza's wilt u hebben?"))
            break
    except: ValueError
    print(f'Je moet wel een getal invullen')

totaal_prijs = Pizza_small_prijs * Pizza_small_aantal + Pizza_medium_prijs * Pizza_medium_aantal + Pizza_large_prijs * Pizza_large_aantal
print(f'De prijs is {totaal_prijs}')

print('------------------------------------------------------------------------------------------------------------')
print('Pizza Rossum')
print(f'{Pizza_small_aantal} kleine pizza :        {Pizza_small_prijs * Pizza_small_aantal}')
print(f'{Pizza_medium_aantal} medium pizza:         {Pizza_medium_prijs * Pizza_medium_aantal}')
print(f'{Pizza_large_aantal} large pizza:          {Pizza_large_prijs * Pizza_large_aantal}')
print(f'totaal_prijs:           {totaal_prijs}')
print('------------------------------------------------------------------------------------------------------------')