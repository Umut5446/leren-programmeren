print('Welcome in the Doors.')
print('Je bent net ergens wakker geworden waar je nog nooit bent geweest.')

deur = input('Je ziet twee deuren kies uit 1 of 2.')
if deur == '1':
  print('Je hebt een aansteker gevonden!')
  print('Je gaat nu door naar een andere kamer, je ziet alweer twee deuren.')
  deur1 = input('Je ziet twee deuren kies uit 3 of 4.')
  if deur1 == '3':
    print('Je hebt een bandage gevonden!')
    print('Je gaat nu door naar een andere kamer, je ziet alweer twee deuren kies uit.')
    deur2 = input('Je ziet nu opeens drie deuren, Je raakt nu nog meer gestrest kies uit: 8, 9 of 10.')
    if deur2 == '8':
      print('KIJK UIT! ER IS EEN MONSTER, HIJ HEEFT JE AANGEVALLEN EN GING SNEL WEGRENNEN!!.')
      print('GEBRUIK SNEL JE BANDAGE!!!')
      print('OHH NEE, de bandage helpt niet echt je gaat langzaam flauwvallen!')
      print('Je hebt het net niet overleefd.')
      print('Game Over!')
      exit()
    elif deur2 == '9':
      print('Je gaat nu door naar en andere kamer!')
      print('Je ziet nu een uitgang')
      print('Je rent nu door maar wanneer je dichterbij kwam zag je dat het gewoon een plaatje was.')
      print('Je wilt terug gaan maar de deur is opslot opeens is de monster achter je en eet je op!')
      print('Game Over!')
      exit()
    elif deur2 == '10':
      print('Ohh NEE, het is heel donker gebruik je aansteker om te kunnen zien waar je naar toe moet gaan.')
      richting = input('Je ziet nu twee wegen kies uit:rechts of links.')
      if richting == 'rechts':
        print('OHH NEE, je bent op een trap gestaan. Je bent nu doodgeplet!!')
        print('Game Over!')
        exit()
      elif richting == 'links':
        print('Je hebt de goede weg gekozen je bent nu weggevlucht van de monster. Je hebt nu een blije leven.')
        print('Completed!')
        exit()
        
  elif deur1 == '4':
    print('Je hebt een sleutel gevonden!') 
    pakken = input('Wil je de sleutel opakken kiest uit: ja of nee.') 
    if pakken == 'nee':
      print('Je pakt de sleutel niet op!')
    elif pakken == 'ja':
      print('Je pakt de sleutel!')
    deur3 = input('Je ziet nu twee deuren kies uit: 5 of 6.')
    if deur3 == '5':
      print('Je hebt niks gevonden dus je gaat maar door.')
      deur4 = input('Je ziet nu opeens drie deuren, Je raakt nu nog meer gestrest kies uit: 11, 12 of 13.')
      if deur4 == '11':
        print('OHH NEE, je ziet die monster achter je. Je pakt je sleutel en steek hem in zijn oog.')
        print('De monster heeft nu heel veel pijn maar hij gaat nogsteeds achter je aan en jij struikelt over je eigen been.')
        print('Je bent nu heel bang de monster kijkt je aan een verslaat je!')
        print('Game Over!')
        exit()
      elif deur4 == '12':
        print('Je hebt een schatkist gevonden en je opent hem met je sleutel. Er zit een granaat in!')
        print('Je hoor iets op je afkomen dus je verstopt ergens. De monster is langsgekomen zijn mond is open je pakt je granaat en gooit hem in zijn mond.')
        print('Het granaat ontploft in zijn maag en is nu in kleine stukken.')
        print('Je kan nu veilig ontsnappen en overleven.')
        print('Completed!')
        exit()
      elif deur4 == '13':
        print('Je ziet dat de deur opslot is dus je opent hem met je sleutel')
        eten = input('je ziet eten je twijfelt of je het moet eten kies uit: ja of nee.')
        if eten == 'ja':
          print('Je bent nu heel sterk en je gaat vechten met de monster de monster geeft jou een hoek maar je slaat hem terug!')
          print('Je geeft hem een trap op zijn hoofd! De monster is nu K.O. gegaan je vlucht nu weg en heb het overleefd.')
          print('Completed!')
          exit()
        elif eten == 'nee':
          print('Je eet het niet op dus je loopt verder maar de monster is daar en je kan hem niet aanvalen.')
          print('Game Over!')
          exit()
    elif deur3 == '6':
      print('Je loopt nu naar de deur maar het is gesloten!')
      sleutel = input('Heb jij je sleutel opgepakt? kies uit: ja of nee.')
      if sleutel == 'nee':
        print('Je kan nu niet meer door!')
      elif sleutel == 'ja':
        print('Je kan nu de deur openen!') 
        print('Je loopt door maar opeens val je naar beneden!')
        print('Je hebt verloren!')
        print('Game Over!') 
        exit()

elif deur == '2':
  print('Je hebt een mes gevonden.')
  deur_1 = input('Je ziet nu twee deuren kies uit: 14 of 15.')
  if deur_1 == '14':
    print('Je ziet een touw. Je snijdt hem nu met je mes.')
    deur_2 = input('Je gaat nu door naar en andere kamer je ziet twee deuren kies uit: 16 of 17.')
    if deur_2 == '16':
      print('Je loopt maar je arm zit opeens vast. Je bent nu bang.')
      snijden = input('Je twijfelt nu of je je arm gaat snijden of niet kies uit: ja of nee.')
      if snijden == 'ja':
        print('Je hebt nu heel veel pijn en een arm verloren maar je overleefd het nog.')
        print('Je bent nu weggevlucht en gaat door met je leven.')
        print('Completed!')
        exit()
      elif snijden == 'nee':
        print('Je durft niet je arm te snijden dus je blijft maar vastzitten en over paar minuten kwam de monster je opeten.')
        print('Game Over')
        exit()
    elif deur_2 == '17':
      print('Je loopt nu door maar je ziet de monster achter je je pakt je mes en steek hem neer.')
      print('De monster gaat nu langzaam dood!') 
      print('Je loopt nu verder maar je ziet opeens iemand daar lopen je houdt je mes nu goed vast en komt langzaam dichterbij.')
      print('Je ziet opeens je vriend! Jullie zijn nu heel blij en gaan samen vluchten.')
      print('Completed!')
      exit()
        
  elif deur_1 == '15':
    print('Je hebt een pistol gevonden!')
    deur_3 = input('Je ziet nu twee deuren kies uit: 18 of 19.')
    if deur_3 == '18':
      print('Je ziet de monster nu achter je je schiet op hem maar je mist.')
      print('OHH NEE, je probeert weer te schieten maar je kogels zijn op.')
      print('De monster is nu dichtbij je en pakt je op en eet je op.')
      print('Game Over!')
      exit()
    elif deur_3 == '19':
      print('Je rent opeens weg omdat je de monster ziet dus je pakt je mes en gooit het op hem.')
      print('De monster heeft pijn maar rent achter je aan jpakt dus je pistol en schiet op hem.')
      print('De monster is nu doodgegaan. Je vlucht nu weg.')
      print('Completed!')
      exit()







   
    
    
    
    
    
    
    
    
    
    
 
