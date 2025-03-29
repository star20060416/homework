def reverse_list(lst):
    new_lst = []
    for i in range(len(lst) - 1, -1, -1):
        new_lst.append(lst[i])
    return new_lst

lst = [1, 'ab', 3, 4.21, "中"]
print(reverse_list(lst))