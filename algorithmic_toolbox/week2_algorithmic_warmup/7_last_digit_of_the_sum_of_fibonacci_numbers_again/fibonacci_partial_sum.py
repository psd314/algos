# Uses python3
import sys


# def fibonacci_partial_sum_naive(from_, to):
#     sum = 0

#     current = 0
#     next = 1

#     for i in range(to + 1):
#         if i >= from_:
#             sum += current

#         current, next = next, current + next

#     return sum % 10


def fib_mod(n, m):
    c = 1
    p = 0
    is_pisano = False
    mods = [0,1]

    i = 2
    while not is_pisano:
        p,c = c, p+c
        mods.append(c % m)

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
    
    sums = []
    total = 0
    for i in range(len(mods)):
        total += mods[i%len(mods)] 
        total %= 10
        sums.append(total)

    return sums[n%len(mods)]

def fib_partial_sum(m, n):
    # if m == 0 return fib_sum(n) ?
    if m == 0:
        return fib_sum(n)
    else:
        Fm = fib_sum(m-1)
        Fn = fib_sum(n)
        result = abs(Fn + 10 - Fm) % 10

        return result


if __name__ == '__main__':
    input = sys.stdin.read()
    from_, to = map(int, input.split())
    print(fib_partial_sum(from_, to))
