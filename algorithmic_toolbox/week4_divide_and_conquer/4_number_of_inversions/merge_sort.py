import sys

def merge(B, C):
    A_prime = []
    i, j = 0, 0
    while i < len(B) and j < len(C):
        b = B[i]
        c = C[j]
        if b <= c:
            A_prime.append(b)
            i += 1
        else:
            A_prime.append(c)
            j += 1
    if i < len(B) - 1:
        A_prime.append(B[i:])
    if j < len(C) - 1:
        A_prime.append(C[j:])
    return A_prime
    
def merge_sort(A):
    if len(A) == 1:
        return A

    m = len(A) // 2
    B = merge_sort(A[:m+1])
    C = merge_sort(B[m+1:])
    A_prime = merge(B, C)
    return A_prime

a = [4, 1, 5, 2, 5]

print(merge_sort(a))