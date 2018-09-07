# Uses python3
import sys

def get_change(m):
    count = 0

    while m > 0:
        if m - 10 >= 0:
            m -= 10
            count += 1
        elif m - 5 >= 0:
            m -= 5
            count += 1
        else:
            m -= 1
            count += 1
    return count

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
