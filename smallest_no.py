num = [11,-45,10,7,1]
smaller_number =num[0]

for i in range(0,len(num)):
        if num[i]<smaller_number:
            smaller_number = num[i]
print(smaller_number)


######################## TC = N.LOGN
num1 = [1,0,-7,-45,10,7,1]
num1.sort()
print(num1[0])



