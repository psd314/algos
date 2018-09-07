# Uses python3
import sys

def optimal_summands(n):
    if n == 1:
        return [1]

    summands = []
    #write your code here
    i = 1
    while n != 0:
        if i <= n :
            n -= i
            summands.append(i)
            i += 1
        else:
            summands[len(summands)-1] += n
            n -= n
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
