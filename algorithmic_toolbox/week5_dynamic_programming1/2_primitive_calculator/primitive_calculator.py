# Uses python3
import sys

def optimal_sequence(n):
    ops = [0]
    for i in range(1, n+1):
        #print('i', i)
        sequence = []
        while i >= 1:
            #print('i', i)
            sequence.append(i)
            #print('seq', sequence)
            if i % 3 == 0:
                i = i // 3
            elif i % 2 == 0:
                i = i // 2
            else:
                i = i - 1

        #print('\n1-ops', ops)
        ops = [ops[0]+1] + ops
        #ops.append(ops[-1]+1)
        print('ops', ops)
        print('seq', sequence)
        # append only the differences from ops and sequence
        if len(sequence) <= len(ops):
            ops = sequence
        # ops.append(min(len(sequence), ops[i-1]+1))
    return reversed(ops)
    #print('len', len(ops))
# compare sequence length to just adding 1?
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
