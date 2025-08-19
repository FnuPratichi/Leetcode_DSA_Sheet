def NewYearParty(n,k):
    problemsolve_minutes = 0
    total_minutes = 0
    count = 0
    for i in range(1,n+1):
        problemsolve_minutes = problemsolve_minutes + 5*i
        total_minutes = problemsolve_minutes + k
        if (total_minutes) > 240:
            break
        else:
            count = count + 1
    print(count)

if __name__ == "__main__":
    n,k = list(map(int,input().split(" ")))
    NewYearParty(n,k)
