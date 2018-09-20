import sys

def merge(a, l, m, r):
    B = a[:m+1]
    C = a[m+1: ]

    i, j, k = 0, 0, 0    
    while i < len(B) and j < len(C):
        if B[i] <= C[j]:
            a[k] = B[i]
            i += 1
        else:
            a[k] = C[j]
            j += 1
        k += 1
    
    while i < len(B):
        a[k] = B[i]
        i += 1
        k += 1
    
    while j < len(C):
        a[k] = C[j]
        j += 1
        k += 1


    return a
    
def merge_sort(A, left, right):
    if len(A) == 1:
        return A

    m = len(A) // 2
    B = merge_sort(A, left, m)
    C = merge_sort(A, m+1, right)
    A_prime = merge(A, left, m, right)
    return A_prime

a = [4, 1, 5, 2, 5]

print(merge_sort(a, 0, len(a)-1))