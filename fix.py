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
name = input('Wat is je naam?')
compliment = input('Hoeveel complimenten wil je hebben?')
for x in range(compliment):
    print(f'Je doet het goed {name}!')