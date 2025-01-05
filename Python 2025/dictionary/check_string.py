#s = input()
def isany_aplha(s):
    is_alphanumeric = False
    for char in s:
        if char.isalnum():
            is_alphanumeric = True
            break
    print("True" if is_alphanumeric else "False")

    is_allaplha = True
    for char in s:
        if char.isalpha():
            is_allaplha = True
            break
    print("True" if is_allaplha else "False")

    isdigit = False
    for char in s:
        if char.isdigit():
            isdigit=True
            break
    print("True" if isdigit else "False")

    islower=False
    for char in s:
        if char.islower():
            islower=True
            break
    print("True" if islower else "False")
    
    isupper = False
    for char in s:
        if char.isupper():
            isupper = True
            break
    print("True" if isupper else "False")     
    
isany_aplha("qa#")








# string = AQ123
# CHAR1 = A , CHAR2 = Q, CHAR3 = 1 , CHAR4 = 2, CHAR4 = 3
# IF ANY OF CHAR IS : ALPHA ---> RETURN TRUE







