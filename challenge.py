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
grootste = 0
kleinste = 1000
aantal_deelbaar_drie = 0
for x in range(10): 
  getal = int(input('voer een getal inboven de (0 en de 1000).'))
  if getal > grootste:
    grootste = getal
  if getal < kleinste:
    kleinste = getal
  
  if getal % 3 == 0:
    aantal_deelbaar_drie = aantal_deelbaar_drie + 1

print(f'Het grootste getal is:{grootste}')
print(f'Het kleinste getal is:{kleinste}')
print(f'Aantal deelbaar door 3 (zonder rest):{aantal_deelbaar_drie} ') 