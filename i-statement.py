from re import A


a = int(input('Geef het grootste getal.'))
b= int(input('Geef het grootste getal.'))

if a > b:
    Max = a
    print(f'a is het grootste getal.')
    max = print(f'Het maximum is: {a}.')
elif a < b:
    Min = b 
    print(f'a is het kleinste getal.')
    min = print(f'Het minimum: is: {b}.')
else:
    print(f'a en b zijn even groot.')
 
