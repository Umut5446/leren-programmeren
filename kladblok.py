# vraag console of pc
# vraag of iemand member is. 15 euro korting indien console
# bereken prijs pc 45 Euro
# consoles 55 Euro

CONSOLE_PRIJS = 55
PC_PRIJS = 45
MEMBER_KORTING = 15

platform = input('Ben je pc of console gamer?')
prijs = PC_PRIJS 

if platform == 'console': 
    prijs = CONSOLE_PRIJS
if input('Bent u member?') == 'Ja':
    prijs = MEMBER_KORTING
else:
        prijs = PC_PRIJS
print(f'U bent {platform} gamer, dan kost de game: {prijs} Euro')

KORTINGS_PRIJS = CONSOLE_PRIJS / 100 * MEMBER_KORTING
totaal_prijs = CONSOLE_PRIJS - KORTINGS_PRIJS

print(f'Met {MEMBER_KORTING} procent korting kost het met member {totaal_prijs}')