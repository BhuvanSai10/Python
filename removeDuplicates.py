def removeDuplicates(l):
    # nl = []
    # for i in l:
    #     if i not in nl:
    #         nl.append(i)
    # return nl
    return list(set(l)) # Order is not maintained

print(removeDuplicates([6,1, 2, 2, 3, 4, 4, 5]))