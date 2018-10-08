#Uses python3
import sys
import math
import random

def dist(x1, y1, x2, y2):
    # print('dist', x1, y1, x2, y2, math.sqrt((x1-x2)**2 + (y1-y2)**2))
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def minimum_distance(a):
    #write your code here
    # print(a)
    
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

    d = min(minimum_distance(s1), minimum_distance(s2))
    #print('d', d)
    middle = -1
    if len(a) % 2 == 0:
        middle = (a[mid][axis] + a[mid-1][axis])/2
    else:
        middle = a[mid][axis]

    a_left = [ s1[i] for i in range(len(s1)) if abs(s1[i][0] - middle ) <= d ]
    a_right = [ s2[j] for j in range(len(s2)) if abs(s2[j][0] - middle ) < = d ]

    a_right.sort(key = lambda: tup: tup[1])

    # for k in a_left
    # a_filtered = [ a[i] for i in range(len(a)) if abs(a[i][axis] - middle) <= d ]
    # a_filtered.sort(key=lambda tup: tup[1])


    # too slow with nested loops
    # for i in range(0, len(a_filtered)-1):
    #     for j in range(i+1, len(a_filtered)):
    #         dst = dist(a[i][0], a[i][1], a[j][0], a[j][1])
    #         d = min(d, dst)
    
    return d
    
    # divide array by 2
    # base case, when array == 2
    # return min val

def brute(a):
    mn_dist = 2000000000
    for i in range(len(a) - 1):
        for j in range(i+1, len(a)):
            dst = dist(a[i][0], a[i][1], a[j][0], a[j][1])
            mn_dist = min(mn_dist, dst)

    return mn_dist

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    a = list(zip(x,y))
    a.sort(key=lambda tup: tup[0])
    
    print("{0:.9f}".format(minimum_distance(a)))
    # a = [(1, 3), (1, 1), (2, 1), (3, 3), (4, 0)]
    
    # a.sort(key=lambda tup: tup[0])
    # print(minimum_distance(a, 0))
    # print(brute(a))
    # equal = True
    # while equal:
    #     a = [ (random.randint(0,5), random.randint(0,5)) for i in range(5) ]
    #     a.sort(key=lambda tup: tup[0])
    #     print(a)
    #     md = minimum_distance(a, 0)
    #     mb = brute(a)
    #     if md != mb:
    #         print('minimum_distance', md)
    #         print('brute', mb)
    #         equal = False