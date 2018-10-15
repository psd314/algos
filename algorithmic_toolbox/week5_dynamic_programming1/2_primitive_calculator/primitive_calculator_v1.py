# Uses python3
import sys

def optimal_sequence(n):
    ops = [0]
    seqs = [[0]]
    for i in range(1, n+1):
        #print('\ni', i)
        sequence = []
        n = i
        while n >= 1:
            #print('n', n)
            #print('while seqs', seqs, 'len', len(seqs))
            #print('seq', sequence)
            if len(seqs) > n:
                sequence += seqs[n]
                #print('sqc', sequence)
                break
            else:
                sequence.append(n)
                if n % 3 == 0:
                    n = n // 3
                elif i % 2 == 0:
                    n = n // 2
                else:
                    n = n - 1

        # ops = [ops[0]+1] + ops
        #print('ops n:', n)
        ops = [seqs[i-1][0]+1] + seqs[i-1]
        #print('ops', ops)
        # need to check all three operations on ops[]
        # then get min  length of ops and compare to brute 
        # force above in while loop
        #print('seqs', seqs)
        #ops.append(ops[-1]+1)
        #print('sequence', sequence)
        # append only the differences from ops and sequence
        if len(sequence) <= len(ops):
            ops = sequence
        # ops.append(min(len(sequence), ops[i-1]+1))
        seqs = seqs + [ops]
    # print('seqs', seqs)
    return reversed(seqs[-1])
    #print('len', len(ops))
# compare sequence length to just adding 1?
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')

# keep shortest for duration of algo
# find shortest 
# store in seqs
# check add 1 to seqs[i][0] and compare to sequence length
# store shortest
