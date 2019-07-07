# pobierz liczbe i sprawdz czy jest pierwsza na funkcjach

def get_number():
    x = int(input('Podaj liczbe:'))
    return x

def is_first(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


def is_end():
    end = input('Kończymy ? t- tak')
    if end == 't':
        return True
    return False


def main_loop():
    while True:
        param = get_number()
        if is_first(param):
            print('To jest liczba pierwsza !!!')
        else:
            print('To nie jest liczba pierwsza ')
        if is_end():
            break

main_loop()

def test_is_first():
    assert is_first(11)
    assert is_first(19)
    assert is_first(37)


def test_is_not_first():
    assert not is_first(12)
    assert not is_first(20)
    assert not is_first(32)

