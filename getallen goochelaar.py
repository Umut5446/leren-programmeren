# optellen, aftrekken, volgorde k / g
getal1 = int(input('Voer getal 1 in:'))
getal2= int(input('Voer getal 2 in:'))
actie = (input('Welke actie wenst u, kies: (o)ptellen, (a)ftrekken'))

antwoord = 0
if actie == 'a':
   antwoord = getal1 - getal2
elif actie == 'o':
   antwoord = getal1 + getal2
elif actie == 'v':
  zin = 'vermenigvuldigen'
elif actie == 'k':
    if getal1 > getal2:
      zin = 'volgorde(k):'  + str(getal2) + ' , ' + str(getal1) 
else:
        zin = 'volgorde(k):' + str(getal1) + ' , ' + str(getal2)       

        print(zin)
if actie != 'k' and actie != 'g':
   print(antwoord)
