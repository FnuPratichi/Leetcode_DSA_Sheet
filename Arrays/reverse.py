# 1. Reverse_number/name

if __name__ == "__main__":
    name = "pratichi"
def reverse(name):
    reversed_name = []
    for n in range(len(name)-1,-1,-1):
        reversed_name.append(name[n])
    print(reversed_name)
reverse(name)

# Reverse digit
def reverse_digit():
    n = 123
    reverse_num = 0
    while(n > 0):
        last_digit = n % 10
        reverse_num = reverse_num*10 + last_digit
        n = n // 10
    print(reverse_num)
reverse_digit()



# Check palindrome
if __name__ == "__main__":
    # s = "ABABA"
    s = "ABCA"
def isPalindrome(s):
    n = len(s)
    i = 0
    j = n-1
    while(i < j):
        if s[i] != s[j]:
            print("Not palindrome")
            return 
        i = i+1
        j = j-1
    print("Palindrome")       
isPalindrome(s)

#find sum from list of numbers
def sum():
    numbers = [1,2,3,4]
    total_sum = 0
    for i in range(0,len(numbers)):
        total_sum = total_sum+numbers[i]
        total_mean = total_sum / len(numbers)
    print(total_sum)
    print(total_mean)
sum()


#find min_max from list of numbers
def minMax():
    numbers = [1,2,4,5,0]
    min_num = numbers[0]
    max_num = numbers[0]
    for i in range(0,len(numbers)):
        if numbers[i] < min_num:
            min_num = numbers[i]
        if numbers[i]> max_num:
            max_num = numbers[i]          
    print(min_num)
    print(max_num)
minMax()


# find primary numbers
import math
def isPrime():
    n = 10
    if n <= 1:
        print(f"{n} is not prime")
        return
    root = int(math.sqrt(n)) + 1
    for i in range(2,root):
        if n % i == 0:
            print("Not prime", i)
    print("prime", i)
isPrime()