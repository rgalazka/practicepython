# 1) bierze liste i tworzy nową z pierwszego i ostatniego elemnetu

a = [5, 10, 15, 20, 25]
# sp 1
c = [x for x in a if x == a[0] or x == a[-1]]

# sp 2
b = []
b.append(a[0])
b.append(a[-1])
print(f'b={b}\n c={c}')


# sp 3
def first_last_list(param):
    ls = []
    ls.append(param[0])
    ls.append(param[-1])
    return ls


def test_first_last_list():
    assert first_last_list([5,]) == [5,5]
    assert first_last_list([5, 10, 15, 20, 25]) == [5, 25]
    assert first_last_list([2, 8, 14, 1, 14, 26]) == [2, 26]
    assert first_last_list([10, 10, 15, 55, 11, 18, 20, 105]) == [10, 105]
    assert first_last_list([13, 10, 'a', 15, 20, 89]) == [13, 89]
