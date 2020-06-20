def binary_search(ls):
    mid = int(len(ls)/2)
    a = [:mid]
    b = [mid:]

    if inp_no in a:
        binary_search(a)
    else:
        binary_search(b)

    return 
