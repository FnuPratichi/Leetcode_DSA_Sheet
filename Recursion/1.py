# Print names n times using recursion and generic way

# generic way 1:

'''names =  input()
times = int(input())
for i in range(times):                   # or you can use :::for _ in range(times):
    print(names)
'''


# generic way 2 : 
'''times=5
def display_names(n):
    count = 0
    for _ in range(times):
        print(n)
        if count > times:
            return
    count=count+1       
display_names('anlku')
'''

# Recursion : using parameters and not by global variables 

"""def fun_names(i,n):
    if i>n:
        return
    print("anku")
    fun_names(i+1,n)
fun_names(1,5)"""


