land1 = input('Land 1?')
land2 = input('Land 2?')
land3 = input('Land 3?')

score_land1 = 0
score_land2 = 0
score_land3 = 0

voor_land1 = 0
voor_land2 = 0
voor_land3 = 0

tegen_land1 = 0
tegen_land2 = 0
tegen_land3 = 0

doelpunten_land1 = 0
doelpunten_land2 = 0
doelpunten_land3 = 0

doelsaldo_land1 = 0
doelsaldo_land2 = 0 
doelsaldo_land3 = 0

print('wedstrijd 1')
doelpunten_land1 = int(input(f'doelpunten: {land1}'))
doelpunten_land2 = int(input(f'doelpunten: {land2}'))

if doelpunten_land2 > doelpunten_land1:
  score_land1 += 3
else:
  score_land2 += 3
 
voor_land1 += doelpunten_land1
tegen_land1 += doelpunten_land2
voor_land2 += doelpunten_land2
tegen_land2 += doelpunten_land1

print('wedstrijd2')
doelpunten_land1 = int(input(f'doelpunten: {land1}'))
doelpunten_land2 = int(input(f'doelpunten: {land2}'))

if doelpunten_land1 > doelpunten_land2:
  score_land1 += 3
else:
  score_land2 += 3
 
voor_land1 += doelpunten_land1
tegen_land1 += doelpunten_land3
voor_land3 += doelpunten_land3
tegen_land3 += doelpunten_land1

print('wedstrijd3')
doelpunten_land1 = int(input(f'doelpunten: {land1}'))
doelpunten_land2 = int(input(f'doelpunten: {land2}'))

if doelpunten_land2 > doelpunten_land3:
  score_land1 += 3
else:
  score_land2 += 3
 
voor_land2 += doelpunten_land2
tegen_land2 += doelpunten_land3
voor_land3 += doelpunten_land3
tegen_land3 += doelpunten_land2
print(f'{land1} : {score_land1} - doelpunten voor: {voor_land1} doelpunten tegen: {tegen_land1}')
print(f'{land2} : {score_land2} - doelpunten voor: {voor_land2} doelpunten tegen: {tegen_land1}')
print(f'{land3} : {score_land3} - doelpunten voor: {voor_land3} doelpunten tegen: {tegen_land1}')

