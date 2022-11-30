# from pickletools import string1
# zin = input('hallo')
# zin2 = 'a'
# for (c) in zin ():
#     zin2 += c
#     print(c)
# ######################################

# teller = 0
# antwoord = ''
# while antwoord != 'stop':
#     antwoord = input('Voer stop in om te stoppen')
#     teller += 1
#     print(teller)

# print(f'aantal enter: {teller}')
#######################################################

# for x in range (0,11,):
#     print(x)
# #######################################################
# x = 0
# while x <= 10:
#     print(x)
#     x += 1
#######################################################
# enc = 'PXDMn!?BdNhP!?eZcoEgBCau!?rxHTfSX!?ixhbV!?cCnlUhFv!?hJFDB!?tDgC!? Uox!?jZzTXPyKq!?uPxQ!?icToHOtRJ!?sscVwqvSfhh!?ttOe!? mAR!?vFzorM!?ebsDQfLcjgR!?rKo!?wnW!?eJGlOGG!?rCTP!?kpVZmoQxP e!?tMohfLBnYtm!?!Vkm'
# next = False
# uitroep_gevonden = False
# vraagteken_gevonden = False
# decrypted_zin = ''

# for c in enc:
#     print(c)
#     print(next)
#     print(uitroep_gevonden)
#     print(vraagteken_gevonden)
    
#     if next:
#         decrypted_zin += c
#         next = False

#     vraagteken_gevonden = c == '?'
#     vraagteken_gevonden and uitroep_gevonden
#     uitroep_gevonden = c == '!'

# print(decrypted_zin)
#############################################################################################################################################################
# grootste = 0
# kleinste = 1000
# aantal_deelbaar_drie = 0
# for x in range(10): 
#   getal = int(input('voer een getal inboven de (0 en de 1000).'))
#   if getal > grootste:
#     grootste = getal
#   if getal < kleinste:
#     kleinste = getal
  
#   if getal % 3 == 0:
#     aantal_deelbaar_drie = aantal_deelbaar_drie + 1

# print(f'Het grootste getal is:{grootste}')
# print(f'Het kleinste getal is:{kleinste}')
# print(f'Aantal deelbaar door 3 (zonder rest):{aantal_deelbaar_drie} ') 
############################################################################################
#vraag 2 woorden, geef vervolgens aan welke letters in beide woorden voorkomen.
# bijv: aapje 
#############################################################################################
# dag_van_week = input('Tot welke dag moet ik printen?')

# while True:
#     print('maandag')
#     if dag_van_week == 'maandag':
#         break
#     print('dinsdag')
#     if dag_van_week == 'dinsdag':
#         break
#     print('woensdag')
#     if dag_van_week == 'woensdag':
#         break
#     print('donderdag')
#     if dag_van_week == 'donderdag':
#         break
#     print('vrijdag')
#     if dag_van_week == 'vrijdag':
#         break
#     print('zaterdag')
#     if dag_van_week == 'zaterdag':
#         break
#     print('zondag')
#     if dag_van_week == 'zondag':
#         break
####################################################################################
# dagen_van_week = ('ma','di','wo','do','vr','za','zo')
# dag_stoppen = input('Tot welke dag moet ik printen?')
# for dag in dagen_van_week:
#     print(dag)
#     if dag == dag_stoppen:
#        break
##############################################################################
# mijnlijst = [5,12,19,27,3,25]     
# print(mijnlijst)
##########################################################################
# mijn_zin = 'hallo dit is mijn zin'
# mijn_zin += '.'
# for c in mijn_zin:
#     print(c)
##########################################
# mijn_eerste_tuple = (1, 2, 3, 4)
# mijn_eerste_lijst = [1, 2, 3, 4]
# mijn_eerste_lijst.append(9)
# mijn_eerste_lijst.remove(3)
# print(mijn_eerste_lijst)

# for x in mijn_eerste_tuple:
#     print(x)
    
# for x in mijn_eerste_lijst:
#     print(x)
###########################################
# antwoorden = []

# for x in range(1,11):
#     antwoorden.append(x * 15)

# print(antwoorden[-1])
#######################################
# namen_lijst = []
# naam = input('Voer een naam in, of quit')
# while naam != 'quit':
#     namen_lijst.append(naam)
# print(namen_lijst)
#################################################
# #1
# mijn_lijst = [5, 12, 19, 27, 3]
# print(mijn_lijst)

# #2
# mijn_lijst.append(25)
# print(mijn_lijst)

# #3
# print(len(mijn_lijst))

# #4
# mijn_lijst.append(12)
# print(mijn_lijst)
# mijn_lijst.remove(12)
# print(mijn_lijst)

# #5
# mijn_lijst.pop(0) 
# print(mijn_lijst)

# #6
# mijn_lijst.insert(0,36)
# print(mijn_lijst)

# #13
# teller = 0
# mijn_lijst = [1, 'aap', 2, 'apen', 3, 'watermeloen', 15, 27]
# for e in mijn_lijst:
#     typ = str(type(e))
#     if typ == "<class ' 'int'>":
#         teller += 1
# print(teller)
##################################################################################
#1
getal = int(input('Kies een getal.'))

for x in range(1, 14):
   print(f'{x} x {getal} = {x * getal}')

#2
mijn_lijst = [5, 12, 19, 27, 3]
print(mijn_lijst)

#3
mijn_lijst.append(25)
print(mijn_lijst)

#4
print(len(mijn_lijst))

#5
mijn_lijst.remove(12)
print(mijn_lijst)

#6
mijn_lijst.remove(5)
print(mijn_lijst)

#7
mijn_lijst.insert(0, 36)
print(mijn_lijst)

#8
for x in(mijn_lijst): 
    print(f'{x}={mijn_lijst}')