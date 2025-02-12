string1 = "This is first string"
string2 = "This is second common string"
string1 = string1.split()
string2 = string2.split()
string3 = string1+string2

new_dict = {}

for key in string3:
    if key in new_dict:
        new_dict[key] = new_dict[key]+1
    else:
        new_dict[key] = 1

for key, value in new_dict.items():
    if value==1:
        print(key)

# way 2:
s1 = "This is first first string"
s2 = "This is second common string common"
words1 = set(s1.split())
words2 = set(s2.split())
print(words1,words2)
# Find uncommon words by taking the set difference
uncommon_words_set = words1.symmetric_difference(words2)
# Convert the set of uncommon words back to a list
uncommon_words_list = list(uncommon_words_set)
print(uncommon_words_list)









