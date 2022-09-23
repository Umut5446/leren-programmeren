croissants = 0.39 * 2
stokbrood = 2.78
kortingsbonnen = 0.50

aantal_croissants = 17
aantal_stokbrood = 2
aantal_kortingsbonnen = 3

croissants = float(input(f'hoeveel kost het croissants per stuk?')) 
croissants = round(croissants,2)
aantal_croissants = int(input(f'Hoeveel stuks croissants heeft u?'))

stokbrood = float(input(f'hoeveel kost het stokbrood per stuk?'))
stokbrood = round(stokbrood,2)
aantal_stokbrood = int(input(f'Hoeveel stuks stokbrood heeft u?'))

kortingabonnen = float(input(f'hoeveel kost het kortingsbonnen?'))
kortingsbonnen = round(kortingsbonnen,2)
aantal_kortingsbonnen = int(input(f'Hoeveel stuks kortingsbonnen heeft u?'))


totaal_prijs_croissants = aantal_croissants * croissants
print("totaal bedrag croissantjes: ",totaal_prijs_croissants)
totaal_prijs_stokbroden = aantal_stokbrood * stokbrood
print("totaal bedrag stokbroden: ",totaal_prijs_stokbroden)
totaal_prijs_kortingsbonnen = aantal_kortingsbonnen * kortingsbonnen
print("totaal bedrag kortingsbonnen: ",totaal_prijs_kortingsbonnen)

totaal_prijs = (aantal_croissants * croissants + croissants + aantal_stokbrood * stokbrood - aantal_kortingsbonnen * kortingsbonnen)

print(f"De feestlunch kost je bij de bakker {totaal_prijs} euro voor de {aantal_croissants} croissantjes en de {aantal_stokbrood} stokbroden als de {aantal_kortingsbonnen} kortingsbonnen nog geldig zijn!")
