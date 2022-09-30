name = 'Umut'
diploma = input('Heb je een bezit van een Diploma MBO-4 ondernemen? J/N')
rijbewijs = input('Heb je een bezit van een vrachtwagen rijbewijs? J/N')
hoed = input('Bezit u een hoge hoed? J/N')
geslacht = input('wat is uw geslacht, man of vrouw?')
snor_breedte = 0
haar = 0
if geslacht == 'man':
    snor = input('Heeft u een snor?')
    snor_breedte = int(input('Hoe breed is u snor?'))
    geslacht_1 = True
elif   geslacht == 'vrouw':
     haar = int(input('hoe lang is u haar?'))
     geslacht_1 = True
lichaamslengte = int(input('Wat is uw netto lichaamslente in hele cm, dus exclusief uw kapsel?'))
gewicht = int(input('Wat is uw lichaamsgewicht in hele kg?'))
certificaat = input('Heeft u een certificaat: Overleven met gevaarlijk personeel? J/N')
ervaring = input('Met welke van de drie heeft u praktijkervaring? kies uit dieren_dresuur, jongleren of acrobatiek.')
dieren_dresuur = 0
jongleren = 0
acrobatiek = 0
if ervaring == 'dieren_dresuur':
    dieren_dresuur = int(input('Hoeveel jaar praktijkervaring heeft u met dieren-dresuur?'))
       
elif ervaring == 'jongleren':
     jongleren = int(input('Hoeveel jaar praktijkervaring heeft u met jongleren?'))
   
elif ervaring == 'acrobatiek':
    acrobatiek = int(input('Hoeveel jaar praktijkervaring heeft u met acrobatiek?'))
  
if diploma == 'J' and rijbewijs == 'J' and hoed == 'J' and lichaamslengte > 150 and lichaamslengte < 220 and gewicht > 90 and gewicht < 120 and certificaat == 'J' and ((geslacht_1 == True and snor_breedte > 10) or (haar > 20)) and dieren_dresuur >= 4 or jongleren >= 5 or acrobatiek >= 3:
         print('Proficiaat! U komt in aanmerking voor een sollicitatiegesprek, stuur snel uw CV.') 
 
else:
       print('U voldoet niet aan aan onze strenge eisen voor de functie circusdirecteur, het spijt ons!')

