print('Hello World')

def fib(n):
    fib = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
        fib.append(a)
    return fib

print(fib(10))

# I made a change!!! by Myeong
