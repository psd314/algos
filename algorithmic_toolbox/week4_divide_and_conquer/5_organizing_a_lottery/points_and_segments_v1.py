# Uses python3
import sys

def fast_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    pairs = []
    indices = {}

    for s in starts:
        pairs.append((s,'l'))
    for p in points:
        pairs.append((p,'p'))
    for e in ends:
        pairs.append((e, 'r'))
    #write your code here
    data = sorted(pairs, key=lambda p: (p[0], p[1]))
    seg = 0
    for d in range(len(data)):
        if data[d][1] == 'l':
            seg += 1
        elif data[d][1] == 'r':
            seg -= 1
        else:
            indices[data[d][0]] = seg
    for p in range(len(points)):
        cnt[p] = indices[points[p]]
    return cnt


def naive_count_segments(starts, ends, points):
    cnt = [0] * len(points)
    for i in range(len(points)):
        for j in range(len(starts)):
            if starts[j] <= points[i] <= ends[j]:
                cnt[i] += 1
    return cnt

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    points = data[2 * n + 2:]
    #use fast_count_segments
    cnt = fast_count_segments(starts, ends, points)
    for x in cnt:
        print(x, end=' ')
