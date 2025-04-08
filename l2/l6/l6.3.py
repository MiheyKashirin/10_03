n=int(input('Введите число:'))
str_n=str(n)
while n>9:
    n=eval('*'.join(str(n)))
print(n)
