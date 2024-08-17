def fib(n):
    if n<=1:
        return n
    last=fib(n-2)
    start=fib(n-1)
    return last+start
print(fib(0))
print(fib(1))
print(fib(2))
print(fib(3))
print(fib(4))
print(fib(5))
print(fib(6))