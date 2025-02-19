#Given a list of numbers, create a function which returns the list but with each element's index in the list added to itself. 
# [0, 0, 0, 0, 0] ➞ [0, 1, 2, 3, 4]

def add_indexes(my_list):
    result = []
    for i in range(0,len(my_list)):
        sum_val = my_list[i]+i
        result.append(sum_val)
    print(result)


add_indexes([0, 0, 0, 0, 0])