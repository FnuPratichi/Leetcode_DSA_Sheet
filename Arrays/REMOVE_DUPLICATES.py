# nums1 = [1,5,3,2]

# def reversed_list1(nums1):
#     reversred_array = sorted(nums1,reverse=True)
#     sorted_array = sorted(nums1)
#     print(reversred_array)
#     print(sorted_array)
# reversed_list1(nums1)


nums = [1,1,1,2,3,4,4]

def remove_num(nums):
    mydict = {}
    for i in range(0,len(nums)):
        mydict[nums[i]]='True'
    print(mydict)

    index = 0
    for key in mydict.values():
        nums[index] = key
        index+=1
    print(index)

remove_num(nums)

# using two pointer

nums1 = [1,1,1,2,3,4,4]

def remove_duplicates(nums1):
    i = 0
    for j in range(1,len(nums1)):
        if nums1[i]!=nums1[j]:
            nums1[i+1] = nums1[j]
            i=i+1
    print(i+1) 

remove_duplicates(nums1)