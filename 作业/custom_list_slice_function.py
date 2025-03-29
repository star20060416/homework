def slice_with_step(mylist, start, step):
    result = []
    for i in range(start, len(mylist), step):
        result.append(mylist[i])
    return result

L1 = [11, 2, 33, 4, 5, 6, 7, 8, 9]
start = 1
step = 2
print(slice_with_step(L1, start, step))