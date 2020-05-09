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
    l = len(inp_alp)
    if inp_str == 'done':
        break
    else:
        for i in range(len(inp_str)):
            ls.append(inp_str[i])
            x = inp_alp.find(inp_str[i])
            m = 2*(l-x) + 1
            if l%2 == 0:
                if m//l == 0:
                    ls[i] = inp_alp[m - 1]
                elif m//l == 1:
                    ls[i] = inp_alp[m//l + m%l - 1]
                else:
                    ls[i] = inp_alp[m%l - 1]
            else:
                if m//l == 0:
                    ls[i] = inp_alp[m - 1]
                else:
                    ls[i] = inp_alp[m%l -1]
    out = ''
    for i in range(len(ls)):
        out = out + ls[i]
    print(out)
