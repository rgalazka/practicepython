"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate.
(Hint: The Fibonnaci seqence is a sequence of numbers where the next number
in the sequence is the sum of the previous two numbers in the sequence.
The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)
"""


def fib_gen(x):
    if x == 1:
        return [1, ]
    if x == 2:
        return [1, 1]
    if x > 2:
        ls = [1, 1]
        for i in range(2, x):
            ls.append(ls[i - 2] + ls[i - 1])
        return ls

print(fib_gen(10))

def test_fib_gen():
    assert fib_gen(3) == [1, 1, 2]
    assert fib_gen(10) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]