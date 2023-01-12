import random

score = 0
geraden = 0
ronde = 0

getal = random.randint(1, 1000)

while True:
    if ronde == 20:
        print("Eindescore = ", score)
        break
    
    while True:
        print(getal)
        raad = int(input("Raad het getal tussen de 1 en 1000."))
        x = getal - raad
        y = raad - getal
        
        if raad == getal:
            print("Goed geraden!")
            score += 1
            ronde += 1
            geraden = 0
            getal = random.randint(1, 1000)
            print("Score = ", score)
        
        elif raad < 0:
            print("Lager!")

        elif raad > getal:
            print("Lager!")
            geraden += 1
            if y < 20 and y >= 0:
                print("Je bent heel warm!")
            elif y < 50 and y >= 20:
                print("Je bent warm!")
        elif raad < getal:
            print("Hoger!")
            geraden += 1
            if x < 20 and x >= 0:
                print("Je bent heel warm!") 
            elif x < 50 and x >= 20:
                print("Je bent warm!")
        
        if geraden == 10:
            print("Score = ", score)
            getal = random.randint(1, 1000)
            ronde += 1
            vraag = input("Nog een getal raden? Y/N ").lower()
            if vraag == "n":
                exit()
            else:
                geraden = 0
                continue
 
    