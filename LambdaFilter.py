list1= [2,31,42,11,6,5,23,24]
newlist= list (filter(lambda x: x % 2 != 0, list1))
print('orginal list is: ',list1)
print('odd numbers from the list is: ',newlist)
