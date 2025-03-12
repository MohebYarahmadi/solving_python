text = input()

happy = text.count(':-)')
sad = text.count(':-(')

if happy == 0 and sad == 0:
    print('none')
elif happy > sad:
    print('happy')
elif happy < sad:
    print('sad')
elif happy == sad:
    print('unsure')

