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
        verschil_raden = abs(getal - raad)
       
        
        if raad == getal:
            print("Goed geraden!")
            score += 1
            ronde += 1
            geraden = 0
            getal = random.randint(1, 1000)
            print("Score = ", score)
        else:
            if raad > getal:
                print("lager")
            else:
                print("lager") 
            geraden += 1
            if verschil_raden < 20:  
                print("Je bent heel warm!")
            elif verschil_raden < 50 and verschil_raden >= 20:
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

 
    