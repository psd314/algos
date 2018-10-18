# Uses python3
def edit_distance(s, t):
    #write your code here
    d = [ [i]+list(range(1, len(t)+1)) if i==0 else [i] + [0]*len(t) for i in range(len(s)+1) ] 
    m = len(s)
    n = len(t)
    
    for i in range(1, m+1):
       for j in range(1, n+1):
        #    print('i', i, 'j', j)
        #    print('s', s[i-1], 't', t[j-1])
        #    print()
           ins = d[i][j-1] + 1
           delete = d[i-1][j] + 1
           match = d[i-1][j-1] 
           mismatch = d[i-1][j-1] + 1
           if s[i-1] == t[j-1]:
               d[i][j] = min(ins, delete, match)
           else:
               d[i][j] = min(ins, delete, mismatch)
    
    # for k in d:
    #     print(k)
    # print('m', m, 'n', n)
    return d[m][n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
