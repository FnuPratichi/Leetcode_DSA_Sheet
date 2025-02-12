# Handle 3 test cases 
#1. if x = 413 then reverse =  314
#2. if x = -413 then reverse = -314
#3. if x overflows the max or min 32 bit signed integer limit then return 0

def reverse_function(x):
    negative_flag = False
    if x < 0 : 
        negative_flag = True
        x = -x # converting negative number to positive for further easy calculations

    reverse_number = 0
    while x!=0:
        last_digit = x % 10  # give the remainder of digit
        reverse_number = reverse_number*10 + last_digit  # appending last digit with the mul of reversed number with 10
        print(reverse_number)  # just to check reverse value everytime
        x = x//10 # to get the integer part of the integer 

    if reverse_number > 2**31-1 or reverse_number < -2**31 : 
        return 0
    # if negative_flag==True:
    #     reverse_number = -reverse_number
    #     print("Hi",reverse_number)

    return reverse_number

print(reverse_function(431))
print(reverse_function(-431))
#print(reverse_function(153478039376920987980009))


