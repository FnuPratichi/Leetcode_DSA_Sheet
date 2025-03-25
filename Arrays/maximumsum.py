# Given an integer array nums, find the subarray with the largest sum, and return its sum.
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

#kadanne's algorithm - TC =O(N)
import sys
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]

def max_sum(nums):
    sum1=0
    maxi = -sys.maxsize - 1
    for i in range(0,len(nums)):
        sum1 = sum1+nums[i]
        if sum1 > maxi :
            maxi = max(sum1,maxi)
        if sum1<0:
            sum1=0
    print(maxi)
max_sum(nums)
