# 1. Parametrized method


def sumfun(n,sum):
    if n<1:
        print(sum)
        return
    sumfun(n-1, sum+n)
sumfun(3,0)


# 2. Functional way :important 

def sumfun(n):
    if n<0:
        return 0   # BASE CASE IF F(0) then zero
    return n+sumfun(n-1)
sumfun(3)

import sys
sys.setrecursionlimit(10**5)     
# 3. sum of cubes 
def cubes_sum(n):
    if n<=0 :
        return 0
    return n**3 + cubes_sum(n-1)
#print(cubes_sum(3))

print(cubes_sum(2935))


