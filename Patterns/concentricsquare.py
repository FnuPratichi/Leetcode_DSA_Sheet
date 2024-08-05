n=5
for i in range(0,2*n-1):
    for j in range(0,2*n-1):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("4",end=' ')
    print(" ")
