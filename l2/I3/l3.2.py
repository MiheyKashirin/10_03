my_list=["Banana","apple","green","music",1991]
if len(my_list)>=1:
    my_list=[my_list[-1]]+my_list[:-1]
print(my_list)


