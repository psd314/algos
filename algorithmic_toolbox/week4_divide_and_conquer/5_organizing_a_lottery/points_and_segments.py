# Uses python3
import sys

def binary_search(val, points, left, right):
    print('first call val:', val, points, 'left:', left, 'right:', right)
    l, r = -1, -1
    if right - left == 0:
        return (left, right)

    mid = ((right - left) // 2) + left
    print('mid:', mid)
    if val == points[mid]:
        if points[mid-1] != val and points[mid+1] != val:
            return (mid, mid)

        if 0 < mid and mid <= len(points)//2 and points[mid-1] == val:
            print('left call')
            l = binary_search(val, points, 0, mid-1)
        elif 0 < mid and mid <= len(points)//2 and points[mid-1] != val:
            l = mid

        if len(points)//2 <= mid and mid < len(points)-1 and points[mid+1] == val:
            print('right call')
            print('val:', val, points, 'mid:', mid, 'right:', right)
            r = binary_search(val, points, mid+1, len(points)-1)
        elif len(points)//2 <= mid and mid < len(points)-1 and points[mid+1] != val:
        # elif mid >= len(points)//2 and mid < len(points)-1 and points[mid+1] != val:
            ('hit right end')
            r = mid
        print('l', l, 'r', r)
        return (l, r)
    elif val < points[mid]:
        return binary_search(val, points, left, mid-1)
    else:
        return binary_search(val, points, mid+1, right)

    # check if midpoint is == val, are there other vals left/right?
    # find left index and right index

    # return tuple of index of leftmost/rightmost value, how to determine which direction?
    # run just binary_search with dummy arrays

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    ordered = sorted(points)
    # print(points, ordered)
    #write your code here
    for i in range(len(starts)):
        if starts[i] == ends[i]:
            count = binary_search(starts[i], ordered, 0, len(points)-1)
        else:
            left = binary_search(starts[i], ordered, 0, len(points)-1)
            right = binary_search(ends[i], ordered, 0, len(points)-1)
            print(left, right)
            # take tuple range
            # calculate number of points
            # update cnt array, search for indexes in points
            # matching search value
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
    points = [1, 2, 3, 3, 3, 4, 5]
    points.sort()
    print(binary_search(3, points, 0, len(points)-1))
    # fast_count_segments([2],[3], points)
    # print(points)
    # print(starts, ends)
    #use fast_count_segments
    # cnt = naive_count_segments(starts, ends, points)
    # for x in cnt:
    #     print(x, end=' ')

# test0 - 1 0 0
# test1 - 0 0 1
# test2 - 2 0

# foreach segment - binary search endpoints in points, get indexes then subtract
# sort points
# get range of indices (duplicates?) and use for count for each segment
