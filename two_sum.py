def twoSum():
    nums = [2,7,11,15]
    target = 9
    
    result = []
    sum=0
    r = result.append(nums[1])
    
    for num in nums:
        sum = r + num 
        if sum == target:
            print(r)




