# 1. print numbers linearly from 1 to N 

def printNos(N):       # IF USING CLASS then use self
        if N < 1:
            return
        printNos(N-1)    # if in class then use self.fun(n-1)
        print(N, end=" ")
printNos(10)



# 2. Print GFG n times

def printGfg(n):
        if n < 1:
            return
        printGfg(n-1)
        print('GFG',end=" ")
printGfg(10)

