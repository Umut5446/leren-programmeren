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
bedrag = int(input('Voer bedrag centen in :')) * 100
 
euro_2 = bedrag // 200
print(f'aantal 2 euro: {euro_2}')
restant = bedrag - euro_2 * 200

euro_1 = restant // 100
print(f'aantal 1 euro: {euro_1}')
restant = restant - 100 * euro_1
 

euro_50 = restant // 50
print(f'aantal 50 cent: {euro_50}')
restant = restant - 50 * euro_50
 

euro_25 = restant // 25
print(f'aantal 25 cent: {euro_25}')
restant = restant - 25 * euro_25
 
