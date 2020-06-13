def fibonacci(n):
    if n<=1:
        return n
    else:
        a = 0
        b = 1
        c = 0

        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return c

print(fibonacci(75))
