# store unique lists of arrays in set

# THIS CAN'T HAPPEN , coz we converted the entore list to tuple but inside the tuple , we still have list which are immutable, so we need to convert each list inside the tuple to tuple

# unique = set()
# my_list = [[1,2,3],[4,5,6],[1,2,3]]
# list_to_tuple = tuple(my_list)

# print(list_to_tuple) 

# unique.add(tuple(my_list))
# print(unique)

unique = set()
my_list = [[1,2,3],[4,5,6],[1,2,3]]
my_dict = {"name":1, "class":2}
my_string = ['a','b']

for li in my_list:
    unique.add(tuple(li))
print(unique)






