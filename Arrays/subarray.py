a = [1,2,3,4]
res = []
def findall_subarray(a):
    for i in range(0,len(a)):
        curr_sub = []
        for j in range(i,len(a)):
            curr_sub.append(a[j])
            res.append(curr_sub[:])
    print(res)


findall_subarray(a)
