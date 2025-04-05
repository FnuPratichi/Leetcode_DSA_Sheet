if __name__ == "__main__":
    n = 5
    r = 3
############## better brute

def findNCR(n,r):
    result = 1
    num = 1
    deno = 1
    for i in range(0,r):
        num = num * (n-i)
        deno = deno * (i+1)
    result = num//deno
    print(result)
findNCR(n-1,r-1)


# def factorial(n,r):
#         fact = 1
#         for i in range(1,n+1):
#               fact = fact*i
#         print(fact)
# factorial(n,r)

# def factNCR(n,r):
#         result_n = 1
#         for i in range(1,n+1):
#               result_n = result_n*i
#         #print(result_n)
#         result_r = 1
#         for i in range(1,r+1):
#               result_r = result_r*i
#         #print(result_r)
#         result_nr = 1
#         for i in range(1,(n-r)+1):
#               print(i)
#               result_nr = result_nr*i
#               print(result_nr)
#         #print(result_nr)
#         result = result_n // (result_r* result_nr)
#         print(result)
# factNCR(n,r)

        
