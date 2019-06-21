nmb = int(input('Podaj liczbe: '))

# sp 1
lista1 = []
for i in range(1, nmb + 1):
    if nmb % i == 0:
        lista1.append(i)
print(lista1)

# sp 2
lista2 = [i for i in range(1, nmb + 1) if nmb % i == 0]
print(lista2)
