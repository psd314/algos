# Uses python3
from sys import stdin

# def fibonacci_sum_squares_naive(n):
#     if n <= 1:
#         return n

#     previous = 0
#     current  = 1
#     sum      = 1

#     for _ in range(n - 1):
#         previous, current = current, previous + current
#         sum += current * current

#     return sum % 10

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    vals = []
    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current
        vals.append(sum)
        
    print(vals)
    return sum % 10

def fib_mod(n, m):
    c = 1
    p = 0
    is_pisano = False
    mods = [0,1]
    total = 1

    i = 2
    while not is_pisano:
        p,c = c, p+c
        total += c**2
        mods.append(total % m)

        if mods[i-1] == 0 and mods[i] == 1:
            is_pisano = True

        i += 1

    return mods[:-2]

def fib_sum(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    mods = fib_mod(n, 10)

    return mods[n%len(mods)]

if __name__ == '__main__':
    n = int(stdin.read())
    print(fib_sum(n))
