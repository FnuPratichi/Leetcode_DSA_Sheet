name_string = input()
name_dict = {}
duplicate_list = []

for char in name_string:
    if char in name_dict:
        name_dict[char] = name_dict[char]+1
    else:
        name_dict[char] = 1
print(name_dict)

for char,i in name_dict.items():
    if i>1:
        duplicate_list.append(char)
print(duplicate_list)
