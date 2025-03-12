nums= [1,2,1,3,4]
def if_Sorted(nums):
    n = len(nums)
    for i in range(1,n):
        if nums[i]>=nums[i-1]:
            continue
        else:
            print("it's not sorted")
            return 
    print('its sorted')
if_Sorted(nums)



nums1 = [1, 1, 2, 1, 3, 14]
def is_sorted(nums1):
    for i in range(1, len(nums1)):
        if nums1[i] < nums1[i - 1]: 
            print('False')
            return  
    print('True')

is_sorted(nums1)


        

