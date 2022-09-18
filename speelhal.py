toegangsticket = 7.45
vip = 0.37
aantal_minuut = 5
aantal_personen = 4
aantal_minuten = 5 * 9
print(aantal_personen * toegangsticket)
print(aantal_personen * 9 * vip)

totaal_prijs = (aantal_personen * toegangsticket + aantal_personen * vip * 9)

print(f"Dit geweldige dagje-uit met {aantal_personen} in de Speelhal met {aantal_minuten} minuten VR kost je maar {totaal_prijs} euro")