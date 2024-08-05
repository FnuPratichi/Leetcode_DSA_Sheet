n=6
for i in range(0,n+1):
    char = ord('A')+i
    for j in range(0,i+1):
        print(chr(char),end='')
    print('')
