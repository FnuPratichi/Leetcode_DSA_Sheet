# find the length of dictionary using len()
dict = {"name" : "anku",
        "age" : 21,
        "date_of_birth" : "11th May"}
print(len(dict.keys()))


# without using len function
count = 0
for key in dict:
    count = count + 1
print(count)





