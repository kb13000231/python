inp_no = input()
ls = list()
x = int(inp_no)
count_5 = 0

while True:
    if x%7 != 0:
        x -= 5
        count_5 += 1
        continue
    else:
        y = int(x/7)
        break

for i in range(count_5):
    ls.append(5)
for i in range(y):
    ls.append(7)

print(ls)
