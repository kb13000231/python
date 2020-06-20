def fibonacci(n):
    if n<=1:
        return n
    else:
        a = 0
        b = 1
        c = 0
        x = []

        for i in range(2,n+1):
            c = a + b
            a = b
            x.append(b)
            b = c
        return x

def factorial(x):
    if x<=1:
        return x
    else:
        z = 1
        for i in range(2,x+1):
            z *= i
        return z


print(fibonacci(10))
