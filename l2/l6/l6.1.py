import string
input_str = "a-A" 
all_letters = string.ascii_letters
start, end = input_str[0], input_str[2]
start_idx = all_letters.index(start)
end_idx = all_letters.index(end)
print(all_letters[start_idx:end_idx + 1])
