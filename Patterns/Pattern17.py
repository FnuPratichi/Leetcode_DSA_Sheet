n=5
for i in range(0,n):
    for j in range(0,n-i):
        print(" ",end='')
    
    char ='A'
    for j in range(0,(2*i)+1):
        print(char,end='')
        char= chr(ord('A')+1)
        
        


    for j in range(0,n-i):
        print(" ",end='')
    print('')
    