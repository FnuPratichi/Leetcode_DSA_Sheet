n=5
for i in range(0,n):
    for j in range(ord('A'),ord('A')+n-i-1): 
        print(chr(j),end='')
    print('')