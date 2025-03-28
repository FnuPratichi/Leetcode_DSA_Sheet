# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
# Example 1:
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.


def longest_subsequence(nums):
    max_length = 0
    for i in range(0,len(nums)):
        num = nums[i]
        count = 1
        for j in range(0,len(nums)):
            if num+1 in nums:
                count = count+1
                num = num+1
        max_length = max(count,max_length)
    print(max_length)

if __name__ == "__main__":
    nums = [0,1,3,2,8]
    longest_subsequence(nums)
