n=5
for i in range(0,2*n-1):
    stars=i
    if i>n:
        stars=((2*n)-i)
    for j in range(0,stars):
        print("*",end='')
    print(' ')