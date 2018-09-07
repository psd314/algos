#Uses python3

import sys

def is_greather_than_or_equal_to(digit, max_dig, res):
    if int(res + str(digit)) >= int(res + str(max_dig)):
        return True

def largest_number(a):
    #write your code here
    res = ""
    while len(a) > 0:
        max_digit = 0
        for i in range(len(a)):
            # if int(a[i]) > max_digit:
            if is_greather_than_or_equal_to(a[i], max_digit, res):
                max_digit = int(a[i])

        res += str(max_digit)
        a.remove(str(max_digit))
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
