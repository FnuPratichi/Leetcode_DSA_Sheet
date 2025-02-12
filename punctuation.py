import string
print(string.punctuation)

my_string = input()
clean_string = ''
for char in my_string:
    if char not in string.punctuation:
        clean_string = clean_string + char
print(clean_string)
