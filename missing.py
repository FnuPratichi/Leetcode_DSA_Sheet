# Create a function that takes a list of numbers between 1 and 10 (excluding one
# number) and returns the missing number.
# Examples
# missing_num([1, 2, 3, 4, 6, 7, 8, 9, 10]) ➞ 5
# missing_num([7, 2, 3, 6, 5, 9, 1, 4, 8]) ➞ 10

# def missing_number(my_list):
#     missing_list = []
#     for num in range(1,len(my_list)+1):
#         if num not in my_list:
#             missing_list.append(num)
#             print(num)
#     print(missing_list)


# missing_number([1, 2, 3, 4, 6, 7, 9, 10])

######## missing number = sum_total(range(1,11) - given sum ) , only app;licable fpr one missing number
def missing_number(my_list):
    total_sum = sum(range(1,11))
    given_sum = sum(my_list)
    missing_num = total_sum-given_sum
    print(missing_num)
missing_number([1, 2, 3, 4, 6, 7, 8,9, 10])

