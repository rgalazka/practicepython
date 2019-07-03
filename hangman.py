from random import randint as rnd

name = input('Podaj imie: ')
print(f'Cześć {name} !!! Czas zagrać w wisielca !!')

ILERAZY = 10
SLOWNIK = ['statek', 'morze', 'zatoka', 'ster', 'kaczka', 'sternik', 'linka', 'burta', 'miecz', 'maszt']

wrd = SLOWNIK[rnd(0, 9)]
print('Zacznij zgadywanie...')
# print(wrd)
buffwrd = []

i = 0
while (i < len(wrd)):
    buffwrd.append('-')
    i += 1
print(buffwrd)

j = 0
while (True):
    sng = input("Podaj litere:")
    k = 0
    while k < len(wrd):
        if wrd[k] == sng:
            buffwrd[k] = sng
        k += 1
    print(buffwrd)
    if '-' not in buffwrd:
        print(f'!!! Wygrałeś {name} !!!!')
        break
    if j == ILERAZY:
        print(f'PRZEGRAŁEŚ {name} - Przekroczona liczba prób !!!')
        break
    j += 1
