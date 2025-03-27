#nums = [1,2,3]
nums = [3,2,1]
# nums = [1,1,5]

def nextPermutation(nums):
    index= -1
    n = len(nums)
    for i in range(n-2,-1,-1):
        if nums[i]<nums[i+1]:
            index = i
            break
    print(index)

    if index == -1:
        nums.reverse()
        print(nums)
    for i in range(n-1,index,-1):
        if nums[index]<nums[i]:
            nums[index], nums[i]  = nums[i],nums[index]
            break
    nums[index+1:] = reversed(nums[index+1:])
    print(nums)


nextPermutation(nums)
