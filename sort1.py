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

tablen = int(input('Podaj długośc tablicy:'))
MAX = 50
i = 0
tab = []
while i < tablen:
    tab.append(rnd(0, MAX))
    i += 1
print(f'Tablicz przed sortowaniem: \n{tab}')
sort(tab)
print(f"Tablica po posortowaniu: \n{tab}")
