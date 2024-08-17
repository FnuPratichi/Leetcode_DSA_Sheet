#1. Check a num 

name=input()
l = len(name)
def check_palin(i):
    if i>=l//2:
        return True
    if name[i]!=name[l-i-1]:
        return False
    return check_palin(i+1)

print(check_palin(0))


# check string using recursion 
def check_palin(name, i, l):
    if i >= l // 2:  # Base case: If we have checked all pairs
        return True
    if name[i] != name[l - i - 1]:  # If characters at the ith position from start and end don't match
        return False
    return check_palin(name, i + 1, l)  # Recursive call with the next index
name = input("Enter a string: ")
l = len(name)
print(l)
print(check_palin(name, 0, l))  # Start checking from index 0



# remove non alphanumeric chara , convert into lowercase and then check
import re
def isPalindrome(s):
    s_new = re.sub(r'[^A-Za-z0-9]','',s).lower()
    print(s_new)
    if s_new == s_new[::-1]:
        print("True")
        print(s_new)
isPalindrome("A man, a plan, a canal: Panama")
