import random
my_list=[random.randint(1,10) for i in range(random.randint(3,10))]
print(my_list)
my_list2=[]
if len(my_list)>=1:
    my_list2.append(my_list[0])
if len(my_list)>=3:
    my_list2.append(my_list[2])
if len(my_list)>=2:
    my_list2.append(my_list[-2])
print(my_list2)
