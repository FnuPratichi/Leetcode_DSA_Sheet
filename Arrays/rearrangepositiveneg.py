# 2149. Rearrange Array Elements by Sign
# You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.
# You should return the array of nums such that the the array follows the given conditions:
# Every consecutive pair of integers have opposite signs.
# For all integers with the same sign, the order in which they were present in nums is preserved.
# The rearranged array begins with a positive integer.
# Return the modified array after rearranging the elements to satisfy the aforementioned conditions.
# Example 1:
# Input: nums = [3,1,-2,-5,2,-4]
# Output: [3,-2,1,-5,2,-4]
# Example 2:
# Input: nums = [-1,1]
# Output: [1,-1]

 
nums = [3,1,-2,-5,2,-4]
def rearrange_neg_postive(nums):
    temp1 = []
    temp2 = []
    for i in range(0,len(nums)):
        if nums[i]>0:
            temp1.append(nums[i])
        else:
            temp2.append(nums[i])
    for i in range(0,(len(nums)//2)):
        nums[2*i] = temp1[i]
        nums[2*i+1] = temp2[i]

rearrange_neg_postive(nums)
print(nums)