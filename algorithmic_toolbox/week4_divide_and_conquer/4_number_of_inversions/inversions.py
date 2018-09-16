# Uses python3
import sys

def merge_sort(a1, a2):
    inversions = 0
    a_prime = []
    i, j = 0, 0
    while i < len(a1) and j < len(a2):
        b = a1[0]
        c = a2[0]
        if b <= c:
            a_prime.append(b)
            i += 1
        else:
            a_prime.append(c)
            inversions += 1
            j += 1
    if i < len(a1) - 1:
        a_prime += a1[i:]
    if j < len(a2) - 1:
        a_prime += a2[j:]

    return inversions
def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    number_of_inversions += merge_sort(a[left:ave], a[ave:right])
    return number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))
