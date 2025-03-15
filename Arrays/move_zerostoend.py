# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# #Brute
# nums = [0,1,0,3,12]

# def move_zeros_toend(nums):
#     temp = []
#     n = len(nums)
#     for i in range(0,n):
#         if nums[i]!=0:
#             temp.append(nums[i])
#     print(temp)
#     x = len(temp)
#     for i in range(0,x):
#         nums[i]=temp[i]
#     for i in range(x,n):
#         nums[i] = 0
#     print(nums)

# move_zeros_toend(nums)
# print(nums)

# optimal

nums1 = [0,1,0,3,12]

def move_zeros_toend1(nums1):
    j = -1
    for i in range(0,len(nums1)):
        if nums1[i]==0:
            j = i
            break
        print(j)
        
    for i in range(j,len(nums1)):
        if nums1[i]!=0:
            nums1[j],nums1[i] = nums1[i],nums1[j]
            j = j+1
    print(nums1)

move_zeros_toend1(nums1)


