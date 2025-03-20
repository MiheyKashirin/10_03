number = int(input('Введите 5-ти значное число:'))
reserved_number = 0

for _ in range(5):
    digit = number % 10
    reserved_number = reserved_number * 10 + digit
    number = number // 10

print(reserved_number)





