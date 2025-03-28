my_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 45, 0, 0, 96, 0]
def move_zeros_to_end(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[count] = lst[i]
            count += 1
    while count < len(lst):
        lst[count] = 0
        count += 1
    print(lst)
move_zeros_to_end(my_list)
