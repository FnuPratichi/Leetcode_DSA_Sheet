# upper complete traingle

n = int(input())
for i in range(0,n):
    for j in range(0,n-i-1):  #this loop is for space
        print(' ',end='')
    for k in range(2*i+1):    #loop for stars
        print('*',end='')
    for m in range(0,n-i-1):  #loop for spaces
        print(' ',end='')
    print(' ')

print()

# lower complete traingle
for i in range(0,n):
    for j in range(0,i):  #this loop is for space
        print(' ',end='')
    for k in range((2*n)-(2*i+1)):    #loop for stars
        print('*',end='')
    for m in range(0,i):  #loop for spaces
        print(' ',end='')
    print(' ')





