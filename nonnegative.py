# Create a function that takes a list of non-negative integers and strings and return a new list without the strings.
# Examples
# filter_list([1, 2, "a", "b"]) ➞ [1, 2]
# filter_list([1, "a", "b", 0, 15]) ➞ [1, 0, 15]

def filter_list(my_list):
    result = []
    for i in range(0,len(my_list)):
        if my_list[i] in range(0,10):
            result.append(my_list[i])
    print(result)

filter_list([1, 2, "a", "b"])
filter_list([1, "a", "b", 0, 15])

######### but to check all integers we can use isinstance(object,class)

def filter_list1(my_list1):
    result = []
    for i in my_list1:
        if isinstance(i,int) and i>0:
            result.append(i)
    print(result)

filter_list1([1, 2, 3, "a", "b"])
filter_list1([1, "a", "b", 0, 15,20])