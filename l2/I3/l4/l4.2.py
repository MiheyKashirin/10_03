lst=[6]
if len(lst) == 0:
    result = 0
else:
    sum_even_indices = 0
    for i in range(0, len(lst), 2):
        sum_even_indices += lst[i]
    result = sum_even_indices * lst[-1]
print(result)
