"""
    Module name :- answer
    Method(s) :- answer()
"""

from solver import solver


def answer():
    """
    Finding the largest palindrome of a product of 2 digit numbers.
    """
    return solver(2)


if __name__ == "__main__":
    print(answer())
