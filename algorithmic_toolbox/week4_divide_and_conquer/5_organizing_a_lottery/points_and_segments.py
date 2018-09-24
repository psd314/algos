# Uses python3
import sys

def binary_search(val, points):
    left = 0
    right = len(points)
    mid = len(points) // 2

    return 0

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    #write your code here
    for i in range(len(starts)):
        if starts[i] == ends[i]:
            cnt = binary_search(starts[i], points)
        else:
            left = binary_search(starts[i], points)
            right = binary_search(ends[i], points)
            cnt[i] = right - left
    return cnt



# def naive_count_segments(starts, ends, points):
#     cnt = [0] * len(points)
#     for i in range(len(points)):
#         for j in range(len(starts)):
#             if starts[j] <= points[i] <= ends[j]:
#                 cnt[i] += 1
#     return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    points.sort()
    print(points)
    print(starts, ends)
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')

# test0 - 1 0 0
# test1 - 0 0 1
# test2 - 2 0

# foreach segment - binary search endpoints in points, get indexes then subtract
