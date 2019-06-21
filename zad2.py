nbr = int(input('Podaj liczbe: '))

if nbr % 2 == 0:
    print('PARZYSTA')
    if nbr % 4 == 0:
        print('Podzielna przez 4')
else:
    print('NIEPARZYSTA')

num = int(input('Podaj Liczbe A: '))
check = int(input('Podaj Liczbe B: '))

if num % check == 0:
    print(f'{num} dzielli sie przez {check} dzieli sie bez reszty - JEST PODZIELNA')
else:
    print(f'reszta z dielenia {num % check} - JEST NIEPODZIELNA')
