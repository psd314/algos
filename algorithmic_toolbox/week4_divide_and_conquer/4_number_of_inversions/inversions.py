# Uses python3
import sys
import random

def merge_sort(a1, a2):
    print('merge')
    print('a1:', a1, 'a2:', a2)
    inversions = 0
    a_prime = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        b = a1[i]
        c = a2[j]
        if b <= c:
            a_prime.append(b)
            i += 1
        else:
            a_prime.append(c)
            inversions += len(a1) - i
            j += 1
        print('a prime_', a_prime)
    if i < len(a1):
        a_prime += a1[i:]
    if j < len(a2):
        print('len a2', len(a2))
        a_prime += a2[j:]
    print('i:', i, 'j:', j)
    print('a prime:', a_prime, '\n')
    return inversions, a_prime

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions, a
    ave = (left + right) // 2
    inv_l, a_l = get_number_of_inversions(a, b, left, ave)
    print('a_l', a_l)
    number_of_inversions += inv_l
    inv_r, a_r = get_number_of_inversions(a, b, ave, right)
    print('a_r', a_r)
    number_of_inversions += inv_r
    inv_s, a_s = merge_sort(a_l, a_r)
    number_of_inversions += inv_s
    return number_of_inversions, a_s

def brute(a):
    inversions = 0
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[i] > a[j]:
                inversions += 1
    return inversions


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print('a:', a, 'len(a)', len(a))
    inv, a_prime = get_number_of_inversions(a, b, 0, len(a))
    print(inv)

    # equal = True
    # i = 0
    # while equal and i < 10000:
    #     a = [ random.randint(1,5) for i in range(6) ]
    #     x = brute(a)
    #     y = get_number_of_inversions(a, [], 0, len(a))

    #     if x != y:
    #         equal = False
    #         print('i:', i)
    #         print('a:', a)
    #         print('brute:', x)
    #         print('solution:', y)
    #     i += 1

