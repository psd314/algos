#Uses python3
import sys
import math

def dist(x1, y1, x2, y2):
    #print('dist', x1, y1, x2, y2, math.sqrt((x1-x2)**2 + (y1-y2)**2))
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def minimum_distance(a):
    #write your code here
    print(a)
    
    if len(a) == 2:
        return dist(a[0][0], a[0][1], a[1][0], a[1][1])
    if len(a) == 3:
        a1, a2, a3 = a[0], a[1], a[2]
        d1 = dist(a1[0], a1[1], a2[0], a2[1]) 
        d2 = dist(a2[0], a2[1], a3[0], a3[1]) 
        d3 = dist(a1[0], a1[1], a3[0], a3[1])
        return min(d1, d2, d3)
    
    mid = len(a) // 2 
    s1 = a[:mid]
    s2 = a[mid:]

    middle = -1
    if len(a) % 2 == 0:
        
    else:
        middle = a[mid][0]

    # filter points > x-mid out
    # sort by y
    # calc remaining dists and return min(d, d')
    d = min(minimum_distance(s1), minimum_distance(s2))
    return d
    
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
    a.sort(key=lambda tup: tup[0])
    print("{0:.9f}".format(minimum_distance(a)))
