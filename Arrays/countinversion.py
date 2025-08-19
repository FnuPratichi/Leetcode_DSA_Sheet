def countinversion(nums):
    count = 0
    for i in range(0,len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]>nums[j]:
                count = count+1
    print(count)

if __name__ == '__main__':
    nums = [5,3,2,4,1]
    countinversion(nums)
