ls= list()
c_5, c_7 = 0, 0

def change(amount):
    global c_5
    global c_7
    if amount%7 !=0:
        amount -= 5
        c_5 += 1
        ls.append(5)
        change(amount)
        return ls

    elif amount==0:
        return ls

    else:
        amount -= 7
        c_7 += 1
        ls.append(7)
        change(amount)
        return ls

change(int(input()))
print('5 coins:',c_5,'7 coins:',c_7)
