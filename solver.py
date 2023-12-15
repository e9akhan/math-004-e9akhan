"""
    Module name :- solver
    Method(s) :- solver(n, p, q)
"""


def solver(n, p=None, q=None):
    """
    Find the largest palindrome number of a product over the given range

    Args:
        n(int) :- length of digits over which to find palindrome number.
        p :- Starting point of the range
        q :- Ending point of the range.

    Return:
        Largest palindrome number of a product over a given range.
    """
    start = 10 ** (n - 1)
    end = p or int("9" * n)

    if p and q:
        start = p
        end = q

    if start > end:
        return None

    palindrome = []

    for x in range(end, start - 1, -1):
        for y in range(x, start - 1, -1):
            value = x * y
            if str(value) == str(value)[::-1]:
                palindrome.append(value)

    if palindrome:
        return max(palindrome)
    return "No palindrome found"


if __name__ == "__main__":
    print(f"solver(2, 1000) = {solver(2, 1000)}")
