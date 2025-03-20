# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.



arr1 = [1,1,2,2,3,3,4]

def single_number(arr1):
    for i in range(0,len(arr1)):
        count = 0
        num = arr1[i]
        for j in range(0,len(arr1)):
            if num == arr1[j]:
                count = count+1
        if count == 1:
            print(num)     
single_number(arr1)


