geel = input('Is de kaas geel?')

if geel == 'ja':
    gaten = input('Zitten er gaten in?')
    if gaten == 'ja':
        print('de gele kaas heeft gaten')
        duur = input('Is de kaas belachelijk duur?')
        if duur == 'ja':
                 print('De kaas die u bedoelt is Emmenthaler.')
        elif  duur == 'nee':
                 print('De kaas die u bedoelt is Leerdammer.')
    elif gaten == 'nee':
         print('De gele kaas heeft geen gaten')
         hard = input('is de kaas hard als steen?')
         if hard == 'ja':
            print('De kaas die u bedoelt is Parmigiano Reggiano.')
         elif hard == 'nee':
               print('De kaas die u bedoelt is Goude Kaas.')
elif geel == 'nee':
    blauweschimmel = input('Heeft de kaas blauweschimmel?')
    if blauweschimmel == 'ja':
        print('De kaas heeft blauweSchimmel.')
        korst = input('Heeft de kaas een korst?')
        if korst == 'ja':
               print('De kaas die u bedoelt is Blue de Rochbaron.')
        elif korst == 'nee':
               print('De kaas die u bedoelt is Foume dAmbert.')
    elif blauweschimmel == 'nee':
               print('De kaas heeft geen blauweschimmel.')
               korst1 = input('Heeft de kaas een korst?')
               if korst1 == 'ja':
                   print('De kaas die u bedoelt is Camembert.')
               elif korst1 == 'nee':
                       print('De kaas die u bedoelt is Mozzarella.')




        
