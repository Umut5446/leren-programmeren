kleuren = ('harten', 'klaveren', 'schoppen', 'ruiten')
soorten = ('boer', 'vrouw', 'heer', 'aas','2', '3', '4', '5', '6', '7', '8', '9', '10',  )
 
kaarten = ['joker1', 'joker2']
for x in range(12):
    for y in range(4):
        kaarten.append(kleuren[y] + ' ' + soorten[x])
print(kaarten)

 