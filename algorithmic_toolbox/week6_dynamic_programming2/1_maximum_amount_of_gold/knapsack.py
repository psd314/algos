# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    w = [0] + sorted(w, reverse=True)
    #print(w)
    value = [ [0]*(W+1) for i in range(len(w)) ]
    for i in range(1, len(w)):
        for j in range(1, W+1):
            #print('i,j', i, j)
            value[i][j] = value[i-1][j]      
            if w[i] <= j:
                val = value[i-1][j-w[i]] + w[i]
                if value[i][j] < val:
                    value[i][j] = val
    count = 0
    #for k in value:
    #    if count == 0:
    #        print(' ',list(range(len(k))))
    #    print(count, k)
    #    count += 1
    return value[n][W]
if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
