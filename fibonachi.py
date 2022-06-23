# O(2^n)
# Memory O(n)
def fib(n):
    if n > 1:
        return fib(n - 1) + fib(n - 2)
    else:
        return n


# O(n)
# Memory O(n)
def fib2(n):
    results = {}
    if n < 2:
        return n
    if n not in results.keys():
        results[n] = fib2(n-1) + fib2(n-2)
    return results[n]


# O(n)
# Memory O(n)
def fib3(n):
    prev = 0
    curr = 1
    for i in range(1, n, 1):
        curr, prev = curr+prev, curr
    return curr


# O(n)
# Memory O(n)
def fib4(n):
    curr = 1
    prev = 0
    if n % 2 == 0:
        for i in range(0, int(n/2), 1):
            prev += curr
            curr += prev
        return prev
    else:
        for i in range(0, int(n/2), 1):
            prev += curr
            curr += prev
        return curr


def run(n):
    print(fib(n))
    print(fib2(n))
    print(fib3(n))
    print(fib4(n))


run(35)
