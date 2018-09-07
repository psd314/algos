# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

def fast_fib(n):

    if n <= 1:
        return n

    nums = [0, 1]
    fib = 0

    i = 1
    while i < n:
        fib = nums[i] + nums[i-1]
        nums.append(fib)

        i += 1

    return fib

n = int(input())
print(fast_fib(n))
