my_list = [10,9,8, 7, 7, 7, 5, 5]
k=5
count = 0
k=k-1


for i in range(0,len(my_list)):
    if my_list[i]>=my_list[k]:
        count +=1
print(count)
