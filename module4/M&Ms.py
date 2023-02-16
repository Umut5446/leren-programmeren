import random

kleuren = ('oranje', 'blauw', 'groen', 'bruin')
aantal = int(input('Hoeveel m&ms wil je in je zakje hebben?'))
zakje = []
for x in range(aantal):
    zakje.append(random.choice(kleuren))
print(zakje)