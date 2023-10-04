my_list=[0,0,0,1,1,13,4,4]
extra_list=[]
duplic_list=[]
i = 0
j = 1
while i < len(my_list):
    if my_list[i] not in extra_list:
        extra_list.append(my_list[i])
    else:
        duplic_list.append(my_list[i])
    i += 1
    
print(duplic_list)