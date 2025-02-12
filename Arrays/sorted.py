nums= [1,2,1,3,4]
n = len(nums)
def if_Sorted(nums):
    for i in range(1,n):
        if nums[i]>=nums[i-1]:
            continue
        else:
            print("it's not sorted")
            return 
    print('its sorted')
if_Sorted(nums)
        

