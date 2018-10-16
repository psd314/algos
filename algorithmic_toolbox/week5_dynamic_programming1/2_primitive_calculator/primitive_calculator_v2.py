# Uses python3
import sys

def optimal_sequence(n):
    ops = [0]
    # seqs = [[0]]
    for i in range(1, n+1):
        # print('\ni', i)
        one = ops[i-1]
        two = n
        three = n
        if i == 1:
            ops.append(0)
            continue
        if i % 3 == 0:
            three = ops[i//3]
        if i % 2 == 0:
            two = ops[i//2]
       
        # print('min ', one, two, three, min(one, two, three))
        ops.append( min(one, two, three) + 1)

    sequence = [n]
    j = len(ops) - 1
    while ops[j] != 0:
        val = j
        one, two, three = ops[j-1], n, n
        if val % 3 == 0:
            three = ops[j//3]
        if val % 2 == 0:
            two = ops[j//2]

        if one <= two and one <= three:
            sequence.append(val-1)
            j -= 1
        elif two <= one and two <= three:
            sequence.append(val//2)
            j //= 2
        else:
            sequence.append(val//3)
            j //=3
        
        
        # test min of three operations

    return reversed(sequence)
    #print('len', len(ops))
# compare sequence length to just adding 1?
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# if n is in array, use array
