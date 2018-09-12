# Uses python3
import sys
import random

def check_majority(a, l, r):
    if l == -1 and r == -1:
        return -1
    elif a.count(l) > len(a)//2:
        return l
    elif a.count(r) > len(a)//2:
        return r
    else:
        return -1
    

def get_majority_element(a, left, right):
    if left == right:
        return a[left]
    if left + 1 == right:
        return a[left]
    #write your code here
    m = len(a) // 2

    l = get_majority_element(a[:m], 0, len(a[:m])-1)
    r = get_majority_element(a[m:], 0, len(a[m:])-1)
    return check_majority(a, l, r)

def brute_force(a):
    for i in a:
        if a.count(i) > len(a)//2:
            return 1

    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)

    # t = brute_force(a)
    # print(f'test: {t}')

    # equal = True
    # i = 0
    # while equal and i < 10000:
    #     a = [ random.randint(0,5) for i in range(10) ]
    #     result = -1
    #     maj = get_majority_element(a, 0, len(a))
    #     brute = brute_force(a)

    #     if maj != -1:
    #         result = 1
    #     else: 
    #         result = 0
    #     if result != brute:
    #         equal = False
    #         print('i', i)
    #         print(f'a: {a}')
    #         print(f'maj: {maj}, brute: {brute}')
    #     i += 1
    # print(f'Done i={i}')
