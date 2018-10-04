#Uses python3
import sys
import math

def dist(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def minimum_distance(a):
    #write your code here
    print(x, y)
    
    if len(x) == 2:
        return dist(a[0][0], a[0][1], a[1][0], a[1][1])
    m = len(a) // 2 

    return math.pi
    
    # divide array by 2
    # base case, when array == 2
    # return min val

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    a = list(zip(x,y))
    print("{0:.9f}".format(minimum_distance(a)))
