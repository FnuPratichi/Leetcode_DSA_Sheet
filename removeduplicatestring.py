# Input: s = "geEksforGEeks"
# Output: "geEksforG"
# Explanation: After removing duplicate characters such as E, e, k, s, we have string as "geEksforG".

s = "geEksforGEeks"
new_dict = {}
for char in s:
    if char in new_dict:
        new_dict[char] = new_dict[char]+1
    else:
        new_dict[char] = 1
print(new_dict)
result = []
for key,values in new_dict.items():
    if values >=1:
        result.append(key)
print(''.join(result))