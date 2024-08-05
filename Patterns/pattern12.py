n=10
space=2*(n-1)
for i in range(0,n):
    for j in range(0,i+1):   # Print the first sequence of increasing numbers
        print(j,end='')
    for j in range(0,space):      # Print the spaces in between
        print(" ",end='')
    for j in range(i,-1,-1):        # Print the second sequence of decreasing numbers
        print(j,end='')             # range(start,stop,step)
    space=space-2
    print(' ')

######################
