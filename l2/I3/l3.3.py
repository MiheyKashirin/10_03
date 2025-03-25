my_list=[1,2,3,4,5,6]
def split_list(lst):
    if len(lst)==0:
        return [[],[]]
    mid=(len(lst) + 1) // 2
    return [lst[:mid],lst[mid:]]
print(split_list(my_list))
print(split_list([1, 2, 3, 4, 5, 6]))
print(split_list([1, 2, 3]))
print(split_list([1, 2, 3, 4, 5]))
print(split_list([1]))
print(split_list([]))