# Uses python3
import sys

def optimal_sequence(n):
    ops = [0]
    for i in range(1, n+1):
        print('i', i)
        sequence = []
        while i >= 1:
            sequence.append(i)
            if i % 3 == 0:
                i = i // 3
            elif i % 2 == 0:
                i = i // 2
            else:
                i = i - 1
        print('sequence', sequence)
        ops.append(min(len(sequence), ops[i-1]+1))
    return ops[1:]
    print('len', len(ops))

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
