my_list = [1,2,3,4,5,6]
if len(my_list) == 0:
    result = [[], []]
else:
    mid = (len(my_list) + 1) // 2
    result = [my_list[:mid], my_list[mid:]]
print(result)