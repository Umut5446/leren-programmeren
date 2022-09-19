Pizza_small_prijs = 4.99
Pizza_medium_prijs = 7.99
Pizza_large_prijs = 9.99

Pizza_small_prijs = float(input(f'Hoeveel kost het pizza small per stuk?'))
Pizza_small_aantal = int(input(f'Hoeveel pizzas wilt u?'))

Pizza_medium_prijs = float(input(f'Hoeveel kost het pizza medium per stuk?'))
Pizza_medium_aantal = int(input(f'Hoeveel pizzas wilt u?'))


Pizza_large_prijs = float(input(f'Hoeveel kost het pizza large per stuk?'))
Pizza_large_aantal = int(input(f'Hoeveel pizzas wilt u?'))

totaal_prijs = Pizza_small_prijs * Pizza_small_aantal + Pizza_medium_prijs * Pizza_medium_aantal + Pizza_large_prijs * Pizza_large_aantal
print(f'De prijs is {totaal_prijs}')

print('------------------------------------------------------------------------------------------------------------')
print('Pizza Rossum')
print(f'Pizza_small_prijs * Pizza_small_aantal:             {Pizza_small_prijs * Pizza_small_aantal}')
print(f'Pizza_medium_prijs * Pizza_medium_aantal:           {Pizza_medium_prijs * Pizza_medium_aantal}')
print(f'Pizza_medium_pijs * Pizza_large_aantal:             {Pizza_large_prijs * Pizza_large_aantal}')
print(f'totaal_prijs:                                       {totaal_prijs}')
print('------------------------------------------------------------------------------------------------------------')