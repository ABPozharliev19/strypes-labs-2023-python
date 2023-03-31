import sys


def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def fibonacci_list(start, end):
    fib = []
    for i in range(start - 1, end):
        fib.append(fibonacci(i))
    return fib


start = int(sys.argv[1])
end = int(sys.argv[2])

fib_list = fibonacci_list(start, end)
print(fib_list)
