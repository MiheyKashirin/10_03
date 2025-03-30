lst=[3,5,6,0,7,9,0,3,12,0,5]
lst0=[]
lst1=[]
for num in lst:
    if num==0:
        lst0.append(num)
    else:
        lst1.append(num)
result=lst1+lst0
print(result)

