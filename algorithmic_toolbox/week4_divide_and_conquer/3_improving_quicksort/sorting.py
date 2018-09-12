# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    j = l
    k = 0
    # print(a, l, r, 'x:', x)
    for i in range(l + 1, r + 1):
        # print(f'i: {i}, j: {j}, a[i]: {a[i]}')
        if a[i] < x:
            # swap from back or front? 
            # to maintain equal region
            if a[i] == x:
                k += 1
            j += 1
            a[i], a[j] = a[j], a[i]
        # if a[i] == x: swap from front?
            # print('k', k, 'swap:', a, '\n')
    a[l], a[j-k] = a[j-k], a[l]
    # print('j-k', j-k, 'j:', j, 'a:', a)
    return j-k, j



# def partition2(a, l, r):
#     x = a[l]
#     j = l
#     for i in range(l + 1, r + 1):
#         if a[i] <= x:
#             j += 1
#             a[i], a[j] = a[j], a[i]
#     a[l], a[j] = a[j], a[l]
#     return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    # print('random index:', k, '\n')
    a[l], a[k] = a[k], a[l]
    #use partition3
    m1, m2 = partition3(a, l, r)
    # print(f'm1: {m1}, m2: {m2} \n')
    randomized_quick_sort(a, l, m1 - 1)
    randomized_quick_sort(a, m2 + 1, r)

def brute(a):
    a.sort()

if __name__ == '__main__':
    # correct recursion depth but solution is timing out now, try Hoare's partition
    # sys.setrecursionlimit(15000) 
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')

    
    
    
    

    # equal = True
    # i = 0
    # while equal and i < 1000000:
        # a = [ random.randint(1,5) for i in range(5) ]
        # 2871
    # a = [ random.randint(1,3) for i in range(10000) ]
    # b = list(a)
    # randomized_quick_sort(b, 0, len(a)-1)

    # if sorted(a) != b:
    #     print(f'i: {i}')
    #     print(a)
    #     print(f'sorted a: {a}')
    #     print(f'quick_sort3 {b}')
    #     equal = False
    
    # i += 1

    
