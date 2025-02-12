my_string = input()
splitted_string = my_string.split()
print(splitted_string)
splitted_string.sort()
for words in splitted_string:
    print(words.capitalize())
