# x = quit
# while x == quit:
#     y = input('Typ iets in!')
#     print(y)
#     print('Als je wilt stoppen typ quit in!')
    
teller = 1

x = input('Typ iets in!') 
while x != 'quit': 
    teller += 1
    x = input('Typ iets in!') 
print(teller)
