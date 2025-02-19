# Write a function that moves all elements of one type to the end of the list.
# Examples move_to_end([1, 3, 2, 4, 4, 1], 1) ➞ [3, 2, 4, 4, 1, 1]

def move_to_end(my_list,element):
    result = []
    count=0
    for i in range(0,len(my_list)):
        if element!=my_list[i]:
            result.append(my_list[i])
        elif element == my_list[i]:
            count = count+1
    print(count)
    print(result)

    for i in range(0,count):
        result.append(element)
    print(result)

move_to_end([1, 3, 2, 4, 4, 1], 1)