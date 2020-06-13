import random

#DICE
while True:
    int = input()
    selected = random.randint(1,6)
    print(selected)
    if int == 'done':
        break
    else:
        continue
