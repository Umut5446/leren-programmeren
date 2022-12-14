# getal = 5
# tekst = 'goeiemorgen' + str(getal)
# print(tekst)
#########################################

# gastheer = input('Wie is de gastheer?')
# gasten = int(input('Hoeveel mensen zijn er?'))
# drank = True
# chips = True

# aanwezigen = gasten if gastheer == '' else gasten + 1
# if gastheer != 'corbijn' and (gastheer == 'umut' or (drank and aanwezigen <= 20 and (gasten >= 4 or gastheer))):
#     print('Start the Party')
# else:
#     print('No Party')
##########################################################################################################################

# name = input('Wat is je naam?')
# compliment = input('Hoeveel complimenten wil je hebben?')
# for x in range(x):
#     print(f'Je doet het goed {name}!')
#######################################################################
# mijn_lijst = ['anton', 'berat', 'cors', 'dirk', 'eduard']
# leeftijd = [16, 17, 12, 29, 15]

# for positie, naam in enumerate (mijn_lijst): 
#     print("hallo", naam, "je bent", leeftijd[positie], "jaar oud")
#######################################################################
# antwoord = input('Voer ja of nee.')

# if antwoord == 'ja' or antwoord == 'nee':
#     print('Het is goed.')
# else:
#     print('Het is niet goed.')

# while True: 
#  antwoord = input('Voer ja of nee.') 
#  if antwoord in ('ja', 'nee'):
#     print('Het is goed.')
#     break
######################################################
# mijn_dict = {
#     123456789: 'Jouke  Corbijn',
#     123456788: 'Jan Janssen',
#     123456787: 'Ogulcan Dinc',
#     123456786: 'Renson Kooij'
# }
# for val in mijn_dict.values():
#     print(val)

# for k in mijn_dict.keys():
#     print(k)

# print(dir(mijn_dict))    

# mijn_lijst = [1]
# print(dir(mijn_lijst))
# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x, y)

# print(thisdict)

# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# x = car.setdefault("model", "Bronco")

# print(x)
##############################################################
# bij een list kan je het veranderen en bij een tuple niet
##############################################################
# programma wat om namen vraagt, om leeftijden vraagt.
# dit opslaat in een dict en vervolgens de hoogste leeftijd print.
# mijn_namen_dict = {}

# while True:
#     naam = input('Wat is je naam? (stop om te stoppen)')
    
#     if naam == 'stop':
#         break
#     if naam in mijn_namen_dict:
#         if input('Wilt u updaten? ja/nee') != 'ja':
#             continue
    
#     leeftijd = int(input('Wat is je leeftijd?'))
#     if leeftijd in mijn_namen_dict.values():
#         print('Let op er zit al iemand in die zo oud is!')
#         for n, l in mijn_namen_dict.items():
#             if l == leeftijd:
#                 break
#         print(f'{n} is al zo oud!')
#         if input('Toch doorgaan? ja/nee') != 'ja':
#             continue

#     # mijn_namen_lijst[naam] = leeftijd
#     mijn_namen_dict.update({naam : leeftijd})

#     print(mijn_namen_dict)

# leeftijd_lijst = list(mijn_namen_dict.values())
# namen_lijst = list(mijn_namen_dict.keys())
# print(leeftijd_lijst)
# print(namen_lijst[leeftijd_lijst.index(max(leeftijd_lijst))])
###############################################################################################
from fruitmand import fruitmand
 
for fruit in fruitmand:
    print(type(fruit))
    print(fruit[round])
    print(fruit)