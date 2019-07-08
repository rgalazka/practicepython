"""
Write a password generator in Python. Be creative with how you generate passwords -
strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.
Extra:
Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
from random import randint as rnd
from string import ascii_letters


def pass_generator(typ, x=8):
    AZ_strong = ascii_letters + '!@#$%^&*()?][}{:;><1234567890'
    AZ_weak = ascii_letters
    i = 0
    pwd = []
    if typ == 'strong':
        zb = AZ_strong
    elif typ == 'weak':
        zb = AZ_weak
    else:
        print('Nie wybrałeś typu hasłą - domyslnie strong')
        zb = AZ_strong

    while i < x:
        pwd.append(zb[rnd(0, len(zb) - 1)])
        i += 1
    return ''.join(pwd)


fl = input('Jakie hasło: (strong /weak):')
ile = int(input('Ile znaków?: '))

print(pass_generator(fl, ile))
