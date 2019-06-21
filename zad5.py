a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

list1 = []
for i in a:
    if i in b and i not in list1:
        list1.append(i)
print(list1)

# ------------- coś tu do poprawy -----------------
list2 = []
list2 = [j for j in a if j in b and j not in list2]
print(list2)

#---------------------------------------------------
from random import randint as rnd

nmb = int(input('Podaj liczbe: '))
ls1, ls2, ls3, i = [], [], [], 0
while i <= nmb:
    ls1.append(rnd(0, 100))
    ls2.append(rnd(0, 100))
    i += 1

for k in ls1:
    if k in ls2 and k not in ls3: ls3.append(k)

print(f' wspólne {ls3}')
