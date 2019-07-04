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
        usr_var = 0;
    elif usr_var == 'k':
        usr_var = 1;
    elif usr_var == 'n':
        usr_var = 2;
    else:
        print("Nie podałeś poprawnej wartości !!!"); break

    rnd_var = rnd(0, 2)
    print(usr_var)
    print(rnd_var)
    stat = input('Gramy ? (k-koniec):')
