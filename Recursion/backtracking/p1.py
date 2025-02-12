# Can you print 1 to N using backtracking?

def pnumber(n):
    if n<1:
        return
    pnumber(n-1)
    print(n)
pnumber(3)

# 1. f(3,3) will execute first and check the 3<1 , no so execute f(2,3)
# 2. f(2,3) will execute and check 2<1 , no so call f(1,3)
# 3. f(1,3) will execute and check 1<1 , no so call f(0,3)
# 4. f(0,3) will execute and check  0<1 , yes so return
# 5. go back to f(1,3) and print i --1
# 6. go back to f(2,3) and print i --2
# 7. go back to f(3,3) and print i --3 


# task 2 : can you print N to 1 using backtracking ?
def printNos(N):       # IF USING CLASS then use self
        if N < 1:
            return    # if in class then use self.fun(n-1)
        print(N)
        printNos(N-1)
printNos(3)
