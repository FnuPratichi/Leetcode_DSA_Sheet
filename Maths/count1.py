name = "ram"
count_list = [0] * 26
for char in name:
    count_list[ord(char) - ord("a")] += 1

print(count_list)

for index in range(len(count_list)):
    count = count_list[index]
    character = chr(index+97)
    if count > 0:
        print(character, count)

'''
pratichi

p, r, a, t, i, c, h

a = [1,10,3,4]

Input: nums = [11,15, -4, 2, 7], target = 9

curr val
curr val + x = target
x = target - curr val

Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

- -
2 7 
2 11
2 15

7 11
7 15

11 15



'''

# def twoSum(nums, target = 9):
#     for i in range(0,len(nums)-1):
#         for j in range(i+1,len(nums)):
#             if (nums[i] + nums[j]) == target:
#                 return [i,j]


