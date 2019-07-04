from random import randint as rnd

def sort(tb):
    k = 0
    while k < len(tb):
        j = 0
        while j < len(tb):
            if tb[k] < tb[j]:
                tb[k], tb[j] = tb[j], tb[k]
            j += 1
        k += 1
MAX = 100
tablen = int(input('Podaj długośc tablicy:'))

tab = [rnd(0, MAX) for i in range(tablen)]
print(f'Tablica przed sortowaniem: \n{tab}')
sort(tab)
print(f"Tablica po posortowaniu: \n{tab}")
