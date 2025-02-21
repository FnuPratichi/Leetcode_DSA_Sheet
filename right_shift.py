# Create a function that takes in two lists and returns True if the second list follows the
# first list by one element, and False otherwise. In other words, determine if the second
# list is the first list shifted to the right by 1.
# Examples
# simon_says([1, 2], [5, 1]) ➞ True
# simon_says([1, 2], [5, 5]) ➞ False
# simon_says([1, 2, 3, 4, 5], [0, 1, 2, 3, 4]) ➞ True
# simon_says([1, 2, 3, 4, 5], [5, 5, 1, 2, 3]) ➞ False
# Notes: Both input lists will be of the same length, and will have 

list1 = [1,2]
list2 = [5,5]
def right_shift(list1,list2):
    is_valid = True  
    
    for i in range(len(list1)):  
        for j in range(len(list2)-1):  
            if i == j and list1[i] != list2[j + 1]:  
                is_valid = False  

    if is_valid:
        print('True')
    else:
        print('False')

right_shift([1,2] ,[5,1])
right_shift([1,2] ,[5,5])
right_shift([1,2,3,4,5] ,[0,1,2,3,4])
right_shift([1,2,3,4,5] ,[5,5,1,2,3])
