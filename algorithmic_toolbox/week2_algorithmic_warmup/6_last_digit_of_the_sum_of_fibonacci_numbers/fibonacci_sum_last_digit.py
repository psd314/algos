# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10

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

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fib_sum(n))
