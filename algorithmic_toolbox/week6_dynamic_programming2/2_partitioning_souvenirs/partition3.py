# Uses python3
import sys
import itertools

def partition3(a):
    if sum(a)%3 != 0 or len(a)<3:
        return 0
    knap = sum(a)//3
    w = [0] + a
    w.sort(reverse=True)
    # print(knap)
    # print('w', w)
    dp = [ [0]*(knap+1) for i in range(len(w)) ]
    for i in range(1, len(w)):
        for j in range(1, knap+1):
            dp[i][j] = dp[i-1][j]
            if w[i] <= j:
                val = dp[i-1][j-w[i]] + w[i]
                if dp[i][j] < val:
                    dp[i][j] = val
    
    # for d in dp:
    #     print(d)
    
    # used1 = [False]*(knap+1)
    used1 = [False]*len(w)
    n = len(w)-1
    W = knap
    if dp[n][W] != knap:
        return 0

    while n >= 0 and W >= 0:
        # print(dp[n])
        # print('n, w', n, W, 'dp[][]', dp[n][W], dp[n-1][W])
        # print()
        if dp[n][W] == dp[n-1][W]:
            n -= 1
        else:
            # print('W', W, used1)
            used1[n] = True
            W -= w[n]
    w1 = [ w[i] for i in range(len(used1)) if used1[i] == False ]
    set1 = [ w[i] for i in range(len(used1)) if used1[i] == True]

    dp1 = [ [0]*(knap+1) for i in range(len(w1)) ]
    for i in range(1, len(w1)):
        for j in range(1, knap+1):
            dp1[i][j] = dp1[i-1][j]
            if w1[i] <= j:
                val = dp1[i-1][j-w1[i]] + w1[i]
                if dp1[i][j] < val:
                    dp1[i][j] = val

    used2 = [False]*len(w1)
    n1 = len(w1)-1
    W1 = knap

    if dp1[n1][W1] != knap:
        return 0

    while n1 >= 0 and W1 >= 0:
        if dp1[n1][W1] == dp1[n1-1][W1]:
            n1 -= 1
        else:
            used2[n1] = True
            W1 -= w1[n1]
    rem = [ w1[i] for i in range(len(used2)) if used2[i] == False]
    set2 = [ w1[i] for i in range(len(used2)) if used2[i] == True]

    if sum(rem) == sum(set1) == sum(set2):
        return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

