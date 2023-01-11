#  #vraag de tijd in uren en minuten
# # en print: Dan duurt de dag nog x uur en y minuten

# vraag = "Hoe laat is het in uren?"
# uren_string = input(vraag)

# uren = int(uren_string)

# print(uren_string)

# #print(f"Dan duurt het nog {23 - uren} uur en {60 - minuten} minuten voordat de dag voorbij is.")

# vraag = "Hoe laat is het in minuten?"
# minuten_string = input(vraag)

# minuten = int(minuten_string)

# print(minuten_string)
########################################################################################################
# a = 3
# if a == 8:
#     b = 5
# print(a)
# if b == 5:
#     print('Ik ben Umut')
#######################################################################################################
# zin = 'hallo wereld'
# x = 0

# for karakter in zin:
#     print(karakter)

# for c in (0,1,2): # 3 rondjes
#     for d in (0,1,2): # 3 rondjes
#         for e in (0,1,2):
#             x += 1
#             print(zin, 'c=', c, 'd=', d, 'e=', e, 'x =', x) 
#######################################################################################################
# prijs = 6.99
# while True:
#     try:
#        hoeveel_pizza = int(input("Hoeveel pizza's wil je hebben"))
#        break
#     except ValueError:
#         print('Je moet wel een getal invullen.')

# bedrag = hoeveel_pizza * prijs 
# print(bedrag)
#######################################################################################################
# if 'woord' in 'zin met woorden':
#     print('woord zit erin')

# richting = 'd'
# while richting not in 'ab':
#     richting = input('Welke kant wil je op? a = links b = rechts')
# if richting not in 'ab':
#     print('Je gaat de verkeerde kant op.')

# try:
#     getal = int(input('Voer een getal!'))
# except:
#     print('Waarschijnlijk begreep je me niet, maar ik bedoelde een geta;l zoals 6')
  
# if 'aa' in 'aapje':
#     print('Er zit aa in')

# if '1' in '123456':
#     print('Er zit 1 in')
# ###############################################################################################
# for x in (0,1,2):
#     print(x)
# # # for element uit verzameling: #vooraf bekende grootte
# # Voor iedere leerling uit klas 22a2
# # voor iedere letter uit een string
# for c in 'zin':
#     print(c)
# x = 10
# while x < 10:
#     print(x) # Ik weet nog niet hoevaak # eindeloze loop

# while True:
#     try:
#         getal = int(input('Voer een getal!'))
#         break
#     except: ValueError
#     print('Waarschijnlijk begreep je me niet, maar ik bedoelde een getal zoals 6')
##########################################################################################################
# x = 100

# while x > 0:
#     x -= 1 

#     print(x, 'bottles of beer on the wall', x, 'bottles of beer on the wall.')
#     print('Take one down and pass it around', {x-1}, 'bottles of beer on the wall')
#     print()
   
#     print('1 bottle of beer on the wall, 1 bottle of beer.')
#     print('Take one down and pass it around, no more bottles of beer on the wall.')
#     print()    
#     print('No more bottles of beer on the wall, no more bottles of beer.')
#     print('Go to the store and buy some more, 99 bottles of beer on the wall')
############################################################################################################
# from msilib.schema import Condition


# for x in range(1, 11, 1):
#     print(type(x))
#     print(x)

# y = 1
# while y < 11:
#     print(y)
#     y += 1
###########################################################################################################
# antwoord = input('Voer ja in')
# while antwoord != 'ja':
#     antwoord = input('Voer ja in')
###############################################################
# for x in range(1000,100,-1):
#     print(x)
###############################################################
# for x in range(-100,2):
#     print(x)
###############################################################
# for t in range(1,11):
#     print('+++++',t,'+++++')
#     for c in range(1,11):
#         print (c * t)    
###############################################################
# sum = 0
# for c in range(5):
#   sum = sum + c
# print(c)

# print(sum)
################################################################
# end = 100
# for c in range(1,end):
#     print(c)
#     end = 50
################################################################
# vraag console of pc
# vraag of iemand member is. 15 euro korting indien console
# bereken prijs pc 45 Euro
# consoles 55 Euro

# from socket import J1939_PGN_ADDRESS_COMMANDED
# from challenge import Verschil_prijs
# from smartphone import Iphone_13_prijs


# CONSOLE_PRIJS = 55
# PC_PRIJS = 45
# MEMBER_KORTING = 15

# platform = input('Ben je pc of console gamer?')
# prijs = PC_PRIJS 

# if platform == 'console': 
#     prijs = CONSOLE_PRIJS
# if input('Bent u member?') == 'Ja':
#     prijs = MEMBER_KORTING
# else:
#         prijs = PC_PRIJS
# print(f'U bent {platform} gamer, dan kost de game: {prijs} Euro')

# KORTINGS_PRIJS = CONSOLE_PRIJS / 100 * MEMBER_KORTING
# totaal_prijs = CONSOLE_PRIJS - KORTINGS_PRIJS

# print(f'Met {MEMBER_KORTING} procent korting kost het met member {totaal_prijs}')


# naam = input(f'Hoe heet je?')
# #########################################################################################
 

# prijs_iphone = int(input('Hoe duur is de iphone?'))
# prijs_galaxy = int(input('Hoe duur is de galaxy'))

# print(prijs_iphone)
# print(prijs_galaxy)

# if prijs_iphone > prijs_galaxy:
#     duurste_telefoon =  'IPHONE'
#     goedkoopste_telefoon = 'GALAXY'
#     prijs_duurste = prijs_iphone
#     prijs_goedkoopste = prijs_galaxy
# else: 
#     duurste_telefoon = 'GALAXY'
#     goedkoopste_telefoon = 'IPHONE'
#     prijs_duurste = prijs_galaxy
#     prijs_goedkoopste = prijs_iphone

# print(f'De {duurste_telefoon} is het duurst, de telefoon kost: {prijs_duurste} Euro')
# print(f'De {goedkoopste_telefoon} is het goedkoopst, de telefoon kost: {prijs_goedkoopste} Euro')

# Verschil_prijs = prijs_iphone - prijs_galaxy
# if Verschil_prijs > 50: 
#     advies_telefoon = 'GALAXY'
# else:
#         advies_telefoon = 'IPHONE'

# print(f'Het advies is dus de {advies_telefoon} te kopen. Verschil: {Verschil_prijs}.')
# ############################################################################################################
 
# ##########################################################################################################
# fysiek = input('Is het spel fysiek?')
# if fysiek == 'ja':
#     bordspel = input('Is het een bordspel?')
#     if bordspel == 'nee':
#         oranje = input('Is het spel oranje?')
#         if oranje == 'ja':
#             print('Het is het kaartspel.')
#         elif oranje == 'nee':
#             print('Het is Sushi go.')
#         elif bordspel == 'ja':
#             treintjes = input('Heeft het sple treintjes?')
#             if treintjes == 'ja':
#                 print('Ticket to ride.')
#             elif treintjes == 'nee':
#                 print('Gatan')
# elif fysiek == 'nee':
#     sport = input('Is het een sportspel?')
#     if sport == 'ja':
#         print('fifa 23.')
#     if sport == 'nee':
#         print('AOE 4')
# #############################################################################################################
# def getbool(letter: str) -> bool:
#     print(letter)
#     if letter == 'a':
#         return True
#     elif letter == 'b':
#         return True
#     elif letter == 'c':
#         return False 
###########################################################################
# a = 'Jan'
# b = 'Umut'
# c = 'Yassine'


# if a == 'Jan' and b == 'Umut' or c == 'Yassine':
#     print('Het feest gaat door')
# else:
#     print('Het feest gaat niet door')
############################################################################
# rekenen = 6
# engels = 4
# nederlands = 5

# if rekenen > 5 and (engels > 5 or nederlands > 5):
#    print('Je mag naar leerjaar 2')
# else:
#     print('Helaas je blijft zitten')
###################################################################################
# variabele = 
# conditie = voorwaarde
# expressie = berekenen
###################################################################################
# bedrag = int(input('Voer bedrag centen in :')) * 100
 
# euro_2 = bedrag // 200
# print(f'aantal 2 euro: {euro_2}')
# restant = bedrag - euro_2 * 200

# euro_1 = restant // 100
# print(f'aantal 1 euro: {euro_1}')
# restant = restant - 100 * euro_1
 

# euro_50 = restant // 50
# print(f'aantal 50 cent: {euro_50}')
# restant = restant - 50 * euro_50
 

# euro_25 = restant // 25
# print(f'aantal 25 cent: {euro_25}')
# restant = restant - 25 * euro_25
#######################################################################################
# leeftijd = int(input('Hoe oud bent u?'))
# if leeftijd >= 18:
#     rijbewijs = input('Heeft u al een rijbewijs')
#     if rijbewijs == 'ja':
#         print('U mag auto gaan rijden.')
#     elif rijbewijs == 'nee':
#         print('U mag niet gaan rijden.')

# else:
#     print('U mag niet gaan rijden.')
#########################################################################################
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
#######################################################################
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
####################################################################################
# bij een list kan je het veranderen en bij een tuple niet
######################################################################################
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
# ###############################################################################################
# from fruitmand import fruitmand
 
# for fruit in fruitmand:
#     print(type(fruit))
#     print(fruit[round])
#     print(fruit)
#########################################
# while True:
#     print('Hallo 1')
#     print('Hallo 2')
#     continue
#     print('Hallo 3')
####################################################
#vraagt een getal aan de gebruiker en geeft deze terug.
# def vraag_een_getal(vraag: str)-> int: # betekent definier = maak aan
#     while True:
#         try:
#            getal = int(input(vraag))
#            break
#         except ValueError:
#             print('Je moet wel een getal invullen!')
#             continue
#     return getal

# leeftijd = vraag_een_getal('Voer leeftijd in:')
# geboortejaar = vraag_een_getal('Voer geboortejaar in:')
# geboortemaand = vraag_een_getal('Voer geboortemaand in:')
# geboortedag = vraag_een_getal('Voer geboortedag in:')

# print(leeftijd)
#########################################################################
# antwoord = input('Wil je iets invoeren').lower()
# print(antwoord)
#############################################################################
# naam = input('Wat is je naam?')
# print(f'hallo {naam}')
################################################################
# def berat(n: int)-> str:
#     zin = f'hallo {n}'
#     return zin

# vraag = 'Hoe heet je'
# naam = input(vraag)
# antwoord = berat(naam)
# print(antwoord)
###########################################################
# waarom functies?
# hergebruik eigen of ander pgm
# logica te verbergen

# naam           input parm             output
def vraag_om_letter(vraag: str) -> str:
    print('Ik roep de functies aan')
    while True:
        letter = input(vraag)
        if len(letter) > 1:
            print('Je moet wel 1 letter invoeren!')
        else:
            return letter

mijn_letter = vraag_om_letter('Voer een letter in:')
print(mijn_letter)
