# 560. Subarray Sum Equals K
# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.
# A subarray is a contiguous non-empty sequence of elements within an array.
# Example 1: Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2: Input: nums = [1,2,3], k = 3
# Output: 2

from collections import defaultdict
if __name__ == "__main__":
    nums = [1,1,1]
    k = 2

def count_subarray_sum_k(nums):
    sum1 = 0
    prefix_sum = 0
    prefix_sum_count = defaultdict(int)
    subarray_count = 0
    prefix_sum_count[0] = 1
    for i in range(0,len(nums)):
        prefix_sum = prefix_sum+nums[i]
        if prefix_sum-k in prefix_sum_count:
            subarray_count = subarray_count+prefix_sum_count[prefix_sum-k]
        prefix_sum_count[prefix_sum] = prefix_sum_count[prefix_sum]+1
    print(subarray_count)
count_subarray_sum_k(nums)

