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

car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.setdefault("model", "Bronco")

print(x)