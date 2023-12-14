def solver(n, p=None, q=None):
    if p!=None and q!=None and p>q:
        return None

    start = 10**(n-1)
    end = p or int('9'*n)

    if p and q:
        start = p 
        end = q

    palindrome = []

    for x in range(end, start-1, -1):
        for y in range(x, start-1, -1):
            value = x*y
            if str(value) == str(value)[::-1]:
                palindrome.append(value)

    if palindrome:
        return max(palindrome)
    return "No palindrome found"

if __name__ == '__main__':
    print(f'solver(2, 1000) = {solver(2, 1000)}')
