#Uses python3

import sys

def lcs2(a, b):
    #write your code here
    m = len(a)
    n = len(b)
    dp = [ [0]*(len(b)+1) for i in range(len(a)+1) ] 
    print('m:', m, 'n:', n)
    for j in range(1, m+1):
        for k in range(1, n+1):
            print('j:', j, 'k:', k)
            print('a[j-1]', a[j-1], 'b[k-1]', b[k-1])
            if a[j-1] == b[k-1]:
                dp[j][k] = dp[j-1][k]+1
            else:
                dp[j][k] = dp[j][k-1]
                print(False, dp[j][k-1])
                for i in dp:
                    print(i)
            print('dp[j][k]', dp[j][k])
            print()
    for l in dp:
        print(l)
    return dp

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
