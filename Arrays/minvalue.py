if __name__ == "__main__":
    nums = [1,4,1,1,9]
def findmin(nums):
    min_value = nums[0]
    for i in range(1,len(nums)):
        if nums[i-1] > nums[i]:
            min_value = min(min_value,nums[i])
    print(min_value)
findmin(nums)