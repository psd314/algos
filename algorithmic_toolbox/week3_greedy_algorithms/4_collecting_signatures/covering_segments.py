# Uses python3
import sys
from collections import namedtuple
from operator import attrgetter

Segment = namedtuple('Segment', 'start end')
# max of start/ min of end ???
def optimal_points(segments):
    points = []
    #write your code here
    for s in segments:
        points.append(s.start)
        points.append(s.end)

    # print(segments)
    # print('sorted', sorted(segments, key=attrgetter('start')))
    segs = sorted(segments, key=attrgetter('start'))

    m = []
    span = Segment(segs[0].start, segs[0].end)
    m.append(span.end)
    for i in range(1, len(segs)):
        if segs[i].start <= span.end:
            start = max(segs[i].start, span.start)
            end = min(segs[i].end, span.end)
            span = Segment(start, end)
            m[-1] = span.end
        else:
            span = Segment(segs[i].start, segs[i].end)
            m.append(span.end)

    return m

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
