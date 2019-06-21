name = input('Podaj swoje imię: ')
age = int(input('Podaj wiek: '))
numb = int(input('Podaj liczbe wyświetleń: '))

i = 1
while i <= numb:
    print(f'{i}) Twoje imię to: {name}, masz {age} lat w {(100 - age) + 2019}r będziesz miał 100 lat')
    i += 1
