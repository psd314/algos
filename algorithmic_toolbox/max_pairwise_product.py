# Uses python3
def max_pairwise_prod(a):
    n = len(a)
    val1 = 0
    val2 = 0

    for i in range(n):
        if a[i] <= val1 and a[i] > val2:
            val2 = a[i]
        elif a[i] > val1:
            val2 = val1
            val1 = a[i]

        

    return val1 * val2

if __name__ == '__main__':
    n = int(input())
    a = [ int(i) for i in input().split() ]
    print(max_pairwise_prod(a))
# n = int(input())
# a = [int(x) for x in input().split()]

# val1 = 0
# val2 = 0

# for i in range(n):
#     if a[i] >= val1:
#         val2 = val1
#         val1 = a[i]
        

# print(val1 * val2)




