def rain_water(ls):
    for i in range(len(ls)):
        if ls[i] > 0:
            a = i
            break
        else:
            continue
    z = []
    for i in range(a+1,len(ls)):
        if ls[i]>=ls[a]:
            b = i
            break
        else:
            z.append(ls[i])
            print(i)
            continue
    c = ls[a]*len(z) - sum(z)

    for i in range(a+1+len(z)):
        ls.remove(a+len(z)-i)

ls = [3,0,2,0,3]
print(rain_water(ls))


# a+1+len(z)+1
