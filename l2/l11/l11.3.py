def is_even(number):
    return (number&1)==0
assert is_even(2494563894038**2) == True
assert is_even(1056897**2) == False
assert is_even(24945638940387**3) == False
print('ok')