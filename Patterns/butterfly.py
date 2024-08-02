n=10
spaces=(2*n)-2
for i in range(0,(2*n)-1+1):
    stars=i
    if i>n:
        stars=(2*n)-i
    for j in range(0,stars+1):
        print("*",end='')
    for j in range(0,spaces+1):
        print(" ",end='') 
    for j in range(0,stars+1):
        print("*",end='')
    print("")
    if i<n:
        spaces=spaces-2
    else:
        spaces=spaces+2