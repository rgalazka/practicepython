"""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order.
For example, say I type the string:
  My name is Michele
Then I would see the string:
  Michele is name My
shown back to me.
"""


def reverse(napis):
    ls = napis.split()
    ls = ls[::-1]
    return ' '.join(ls)


def test_reverse():
    assert reverse('ala ma kota') == 'kota ma ala'
    assert reverse('Ala ma dużego Kota ') == 'Kota dużego ma Ala'
    assert reverse('ala') == 'ala'
