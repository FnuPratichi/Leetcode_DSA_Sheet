# Time complexity is O(N)
def check_divisor(N):
    sum = 0
    for i in range(1,N+1):
        if N % i== 0:
            print(i)
            sum=sum+i
    print("sum of all divisors ",sum)
check_divisor(36)

print("######################################################")

# CAN WE DO THIS IN O(sqrt(N))?
import math
def check_div(n):
    sq_rt = int(math.sqrt(n))
    for i in range(1,sq_rt):
        if n % i==0:
            print(i)
        if n//i != i:
            print(n//i)
check_div(36)

print("############################################################")
# another way 
import math
def div_check(n):
    divisors = set()
    square_root = int(math.sqrt(n))
    for i in range(1,square_root+1):
        if n % i==0:
            divisors.add(i)
            divisors.add(n//i)
            print(i)
    print(sorted(divisors))
    
div_check(12)
        


