num = [11,20,10,0,15]

largest_num = num[0]
second_largest = -1

for i in range(0,len(num)):
    if num[i] > largest_num:
        second_largest = largest_num
        largest_num=num[i]
print('largest number is' , largest_num)

if num[i] > second_largest and num[i]!=largest_num:
    second_largest = num[i]
print('second largest no is', second_largest)


#always think like B1 --B2---B3 and see where does arr[i] can be and then assign values