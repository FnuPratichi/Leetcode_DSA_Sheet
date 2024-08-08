def check_string(word):
    i=0
    j=len(word)-1
    while(j>i):
        if word[i] != word[j]:
            return 0
        else:
            i=i+1
            j=j-1
    return 1      
print(check_string("BilliB"))