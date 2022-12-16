lang = 8 
breed = 3
diep = 1.5
uitgraven = 25
afvoeren_grond = 32.50

inhoud = lang * breed * diep
uitgraven_kosten = uitgraven * inhoud
afvoeren_grond_kosten = afvoeren_grond * inhoud
totaal_prijs = uitgraven_kosten + afvoeren_grond_kosten

print(f'offerte van een zwembad van {lang} bij {breed} bij {diep} meter(inhoud: {inhoud}m3')

print(f'uitgraven:            {uitgraven_kosten}')
print(f'afvoeren_grond:       {afvoeren_grond_kosten}')
print(f'totaal:               {totaal_prijs}')


afstand = ''
if afstand > 50: