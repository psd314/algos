# Uses python3
import sys

def get_change(m):
    coins = [1, 3, 4]
    min_coins = [0] * (m+1)
    for i in range(1, m+1):
        min_coins[-1] = m
        for j in range(len(coins)):
            if i >= coins[j]:
                num_coins = min_coins[i - coins[j]] + 1
                if num_coins < min_coins[i]:
                    min_coins[i] = num_coins

    #write your code here
    return min_coins[-1]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
