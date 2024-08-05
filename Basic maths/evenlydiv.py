N=2446
count=0
N_new=str(N)
for char in N_new:
    digit=int(char)
    if digit!=0 and N%digit==0:
        count=count+1
print(count)


#Input: n = 2446
#Output: 1
#Explanation: Here among 2, 4, 6 
#only 2 divides 2446 evenly while 4 and 6 do not.
        