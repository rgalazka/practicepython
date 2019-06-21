a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for i in a:
    if i < 5:
        print(f' {i}', end='')
print('\n')

# extr 1
list = []
for j in a:
    if j < 5:
        list.append(j)
print(list)

# extr 2
list2 = [g for g in a if g < 5]
print(list2)

# extr 3
nmb = int(input('Podaj liczbe: '))
lista3 = [k for k in a if k < nmb]
print(lista3)
