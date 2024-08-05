def isPalindrome(x):
    dup = x
    reverse_num = 0
    negative_flag = False
    if x<0:
        negative_flag = True
        x = -x
    while x!=0 : 
        ld = x % 10
        reverse_num = reverse_num * 10 + ld
        x = x//10
            
    if dup == reverse_num : 
        print("True")
    else:
        print ("False")
isPalindrome(121)
isPalindrome(-121)
isPalindrome(10)

        
        