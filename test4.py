import math_fxn
for i in range(100000):
    x = math_fxn.fibonacci(i)
    y = math_fxn.factorial(i)

    if x>y:
        print(i)
        break
print('no result')
