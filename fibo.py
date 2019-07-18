# Fibonacci numbers module

def fib2():   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while b < 1000:
        result.append(b)
        a, b = b, a+b
    return result