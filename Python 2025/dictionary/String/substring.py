string = "SUBS"
new_substring = []

for i in range(len(string)+1):
    for j in range(i+1,len(string)+1):
      new_substring.append(string[i:j])
print(new_substring)

print(new_substring[0:1])



