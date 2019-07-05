from random import randint as rnd

end = ''
while end != 'exit':
    y = rnd(1, 9)
    tab = []
    print('Zaczynamy nową gre:')
    while True:
        x = int(input('Zgadnij liczbę (od 1 do 9):'))
        tab.append(x)
        if x < y:
            print('za mała')
        elif x > y:
            print('za duża')
        else:
            print(f'Brawo - zgadłeś liczba to {y}\n Twoje ruchy: {tab}')
            break
    end = input('Jesli chcesz skończyć wpisz exit jeśli nie dowolny klawiz')
