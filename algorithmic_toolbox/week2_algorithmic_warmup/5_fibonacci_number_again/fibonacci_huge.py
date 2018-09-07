# Uses python3
import sys

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m

def fib_mod(n, m):
    c = 1
    p = 0
    is_pisano = False
    mods = [0,1]

    i = 2
    while not is_pisano:
        t = c
        c += p
        p = t
        mods.append(c % m)

        if mods[i-1] == 0 and mods[i] == 1:
            is_pisano = True

        i += 1
    m = mods[:-2]
    return m[n % len(m)]

if __name__ == '__main__':
    input = sys.stdin.read()
    n, m = map(int, input.split())
    print(fib_mod(n, m))
