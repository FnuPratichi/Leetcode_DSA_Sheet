def check_armstrongNum(x):
    sum=0
    dup_value=x
    no_digit=0
    while x!=0:
        last_digit=x%10
        sum=sum+(last_digit*last_digit*last_digit)
        x=x//10
    if sum==dup_value:
        print('Armstrong Number')
        print(sum)
    else:
        print('Not an armstrong number')
        print(sum)
check_armstrongNum(371)
check_armstrongNum(1634)


# this code will not handle 4 digits number 

def general_armcode(x):
    size=len(str(x))
    print(size)
    sum=0
    dup_value=x
    while x!=0:
        last_digit=x%10
        sum=sum+(last_digit**size)
        x=x//10
    if sum==dup_value:
        print('Armstrong Number')
        print(sum)
    else:
        print('Not an armstrong number')
        print(sum)
general_armcode(371)
general_armcode(1634)


