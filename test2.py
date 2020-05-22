a = 'asdfghjkl'
b = 'asdfrdfg'
ls = list()
for i in b:
    if i in a:
        print('s')
        ls.append(i)
        continue
    else:
        print('f')
        break
print(ls)
