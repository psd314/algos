#Uses python3
import sys
import math
import random

def dist(x1, y1, x2, y2):
    # print('dist', x1, y1, x2, y2, math.sqrt((x1-x2)**2 + (y1-y2)**2))
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)

def minimum_distance(ax, ay):
    #write your code here
    # print('ax', ax)
    
    if len(ax) == 2:
        return dist(ax[0][0], ax[0][1], ax[1][0], ax[1][1])

    if len(ax) == 3:
        ax1, ax2, ax3 = ax[0], ax[1], ax[2]
        d1 = dist(ax1[0], ax1[1], ax2[0], ax2[1]) 
        d2 = dist(ax2[0], ax2[1], ax3[0], ax3[1]) 
        d3 = dist(ax1[0], ax1[1], ax3[0], ax3[1])
        return min(d1, d2, d3)
    
    mid = len(ax) // 2 
    s1 = ax[:mid]
    s2 = ax[mid:]

    d = min(minimum_distance(s1, ay), minimum_distance(s2, ay))
    #print('d', d)
    middle = -1
    if len(ax) % 2 == 0:
        middle = (ax[mid][0] + ax[mid-1][0])/2
    else:
        middle = ax[mid][0]
    # generator???
    # do minimum_dist again on y version???
    # maybe an 'x', 'y' version for minimum_dist???
    # y version is broken, see array below
    a_filtered = [ ay[i] for i in range(len(ay)) if abs(ay[i][0] - middle) <= d ]
    # print('filter', a_filtered, d)
    # mid_y = len(a_filtered) // 2
    # sy1 = a_filtered[:mid_y]
    # sy2 = a_filtered[mid_y:]
    # y_dist = min(minimum_distance(sy1, 1), minimum_distance(sy2, 1))
    # print('y', y_dist)
    # print('d', d)
    # y_dist = 2000000000
    # broken, probably need to do though
    # if len(a_filtered) > 0:
    #     print('filtered', a_filtered)
    #     y_dist = minimum_distance(a_filtered, 1)

    # too slow with nested loops
    for i in range(0, len(a_filtered)-1):
        for j in range(i+1, len(a_filtered)):
            dst = dist(a_filtered[i][0], a_filtered[i][1], a_filtered[j][0], a_filtered[j][1])
            d = min(d, dst)
    
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
    ax = sorted(a, key=lambda tup: tup[0])
    ay = sorted(a, key=lambda tup: tup[1])
    print("{0:.9f}".format(minimum_distance(ax, ay)))
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