print('Do you want to use your own alphabet for encoding or the default 0-z.')
while True:
    inp_alp_bool = input('Type "y" to type your own alphabet, "n" to choose the default one and "done" if completed: ')
    if inp_alp_bool == 'y':
        inp_alp = input('Please enter the alphabet: ')
    elif inp_alp_bool == 'done':
        break
    elif inp_alp_bool == 'n':
        inp_alp = '0123456789abcdefghijklmnopqrstuvwxyz'
    else:
        print('Incorrect response please type y or n')
        continue
    inp_str = input("Please enter the words that you want to encode or done if you're done encoding: ")
    ls = list()
    if inp_str == 'done':
        break
    else:
        for i in range(len(inp_str)):
            ls.append(inp_str[i])
            x = inp_alp.find(inp_str[i])
            m = 2*(x+1)
            if m<=len(inp_alp):
                ls[i] = inp_alp[m - 1]
            else:
                a = m - 2*(len(inp_alp)//2) - 2
                ls[i] = inp_alp[a]
    out = ''
    for i in range(len(ls)):
        out = out + ls[i]
    print(out)
