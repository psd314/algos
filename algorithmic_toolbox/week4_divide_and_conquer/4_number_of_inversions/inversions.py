# Uses python3
import sys
import random

def merge_count(A, B):
    inv = 0
    a_prime = []
    i, j = 0, 0
    while i < len(A) and j < len(B):
        if A[i] > B[j]:
            a_prime.append(B[j])
            inv += len(A) - i
            j += 1
        elif A[i] <= B[j]:            
            a_prime.append(A[i])
            i += 1
    if len(A) - i >= 1:
        a_prime += A[i:]
    if len(B) - j >= 1:
        a_prime += B[j:]
    return inv, a_prime

def get_number_of_inversions(a):
    number_of_inversions = 0
    if len(a) <= 1:
        return number_of_inversions, a
    m = len(a) // 2
    inv, a_l = get_number_of_inversions(a[:m])
    number_of_inversions += inv
    inv, a_r = get_number_of_inversions(a[m:])
    number_of_inversions += inv
    #write your code here
    inv, a_prime = merge_count(a_l, a_r)
    number_of_inversions += inv
    return number_of_inversions, a_prime

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
    print(get_number_of_inversions(a)[0])

# equal = True
# i = 0
# while equal and i < 100000:
#     a = [ random.randint(1,5) for i in range(6) ]
#     x = brute(a)
#     y = get_number_of_inversions(a)[0]

#     if x != y:
#         equal = False
#         print('i:', i)
#         print('a:', a)
#         print('brute:', x)
#         print('solution:', y)
#     i += 1

#solved