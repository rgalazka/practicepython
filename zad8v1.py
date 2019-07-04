from random import randint as rnd

MZ = ['kamień', 'nożyce', 'papier']
# 0 bije 1
# 1 bije 2
# 2 bije 0

stat = ''
while stat != 'k':
    usr_var = input("""
                    Wybierz wartość:
                        Papier - p
                        Kamień - k
                        Nożyce - n\n   
                    """)
    if usr_var == 'p':
        usr_var = 2;
    elif usr_var == 'k':
        usr_var = 0;
    elif usr_var == 'n':
        usr_var = 1;
    else:
        print("Nie podałeś poprawnej wartości !!!");
        break

    rnd_var = rnd(0, 2)

    if usr_var == 0 and rnd_var == 1 or usr_var == 1 and rnd_var == 2 or usr_var == 2 and rnd_var == 0:
        print(f'''
        WYGRAŁEŚ
        Komputer - {MZ[rnd_var]} 
           Gracz - {MZ[usr_var]}
        ''')
    elif usr_var == rnd_var:
        print('Remis')
    else:
        print('Przegrałeś')

    stat = input('Gramy ? (k-koniec):')
