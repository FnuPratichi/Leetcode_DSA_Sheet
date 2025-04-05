list1 = [1,2,3,4]

def reverse_num(list1):
    reverse_list = list1[::-1]
    print(reverse_list)
reverse_num(list1)


#################################

nums = [1, 2, 3, 4, 5]
left = 0
right = len(nums) - 1

while left < right:
    nums[left], nums[right] = nums[right], nums[left]  
    left += 1
    right -= 1

print(nums)  


 

