# Uses python3
import sys
import itertools

def partition3(a):
    if sum(a)%3 != 0 or len(a)<3:
        return 0
    knap = sum(a)//3
    w = [0] + a
    print(knap)
    print('w', w)
    dp = [ [0]*(knap+1) for i in range(len(w)) ]
    for i in range(1, len(w)):
        for j in range(1, knap+1):
            dp[i][j] = dp[i-1][j]
            if w[i] <= j:
                val = dp[i-1][j-w[i]] + w[i]
                if dp[i][j] < val:
                    dp[i][j] = val
    for d in dp:
        print(d)
    
    used1 = [False]*(knap+1)
    n = len(w)-1
    W = knap

    while n >= 0 and W >= 0:
        print(dp[n])
        print('n, w', n, W, 'dp[][]', dp[n][W], dp[n-1][W])
        print()
        if dp[n][W] == dp[n-1][W]:
            n -= 1
        else:
            print('W', W, used1)
            used1[n] = True
            W -= w[n]

    print(used1)


    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))

