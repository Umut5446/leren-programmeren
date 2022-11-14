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
#  #############################
# a = 3
# if a == 8:
#     b = 5
# print(a)
# if b == 5:
#     print('Ik ben Umut')
##########################################################
# zin = 'hallo wereld'
# x = 0

# for karakter in zin:
#     print(karakter)

# for c in (0,1,2): # 3 rondjes
#     for d in (0,1,2): # 3 rondjes
#         for e in (0,1,2):
#             x += 1
#             print(zin, 'c=', c, 'd=', d, 'e=', e, 'x =', x) 
#############################################################
# prijs = 6.99
# while True:
#     try:
#        hoeveel_pizza = int(input("Hoeveel pizza's wil je hebben"))
#        break
#     except ValueError:
#         print('Je moet wel een getal invullen.')

# bedrag = hoeveel_pizza * prijs 
# print(bedrag)
########################################################################################
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

y = 1
while y < 11:
    print(y)
    y += 1
###########################################################################################################
# antwoord = input('Voer ja in')
# while antwoord != 'ja':
#     antwoord = input('Voer ja in')
##################################################
# for x in range(1000,100,-1):
#     print(x)
#####################################
# for x in range(-100,2):
#     print(x)
##########################################
# for t in range(1,11):
#     print('+++++',t,'+++++')
#     for c in range(1,11):
#         print (c * t)    
########################################
# sum = 0
# for c in range(5):
#   sum = sum + c
# print(c)

# print(sum)
######################################
# end = 100
# for c in range(1,end):
#     print(c)
#     end = 50