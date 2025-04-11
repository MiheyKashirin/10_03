def add_one(some_list):
    number = int(''.join(map(str, some_list)))
    number += 1
    return [int(digit) for digit in str(number)]
assert add_one([1, 2, 3, 4])
print(add_one([1,2,3,4]))
assert add_one([9, 9, 9])
print((add_one([9,9,9])))
assert add_one([0]) == [1]
print(add_one([0]))
assert add_one([9]) == [1, 0]
print(add_one([1,0]))

