def fact(x):
    if x<=1:
        return x
    else:
        z = 1
        for i in range(2,x+1):
            z *= i
        return z
print(fact(5))
