# Input: s = "testsample"
# Output: 'e'
# Explanation: e is the character which is having the highest frequency.
# Input: s = "output"
# Output: 't'
# Explanation:  t and u are the characters with the same frequency, but t is lexicographically smaller.

s = "output" 
my_dict = {}
for char in s:
    if char in my_dict:
        my_dict[char]=my_dict[char]+1
    else:
        my_dict[char] = 1
print(my_dict)

sorted_dict = sorted(my_dict.items(), key = lambda x : (-x[1],x[0]))
result = sorted_dict[0][0]
print(result)
