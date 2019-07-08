"""
Write a program (function!) that takes a list and returns a new list that contains
all the elements of the first list minus all the duplicates.
Extras:
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def no_duplicate(a, b):
    a, b = set(a), set(b)
    c = list(a - b)
    return c


def test_no_duplicate():
    assert no_duplicate([1, 5, 9, 10], [0, 5, 10, 12, 13]) == [1, 9]
    assert no_duplicate([1, 5], [0, 5]) == [1, ]
    assert no_duplicate([1, 1, 1, 1], [1, 2, 2, 2, 2]) == []
