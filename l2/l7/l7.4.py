def common_elements():
    lst1=[x for x in range(100) if x%3==0]
    lst2=[x for x in range(100) if x%5==0]
    print(lst1)
    print(lst2)
    set1=set(lst1)
    set2=set(lst2)
    set3= set1 & set2
    print(set3)

common_elements()

