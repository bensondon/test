# L = [x * x for x in range(1, 10)]
# print L

# L=(x * x for x in range(1,10))
# for g in L:
#        print g

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print b
#         a, b=b, a + b
#         n = n + 1
#
# print fib(21)


def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def fib_islice(start, stop, step=1):
    return [num for idx, num in zip(range(stop), fib()) if idx >= start][::step]


print(fib_islice(3, 10))
