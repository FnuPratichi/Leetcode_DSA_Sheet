#brute way:
# time complexity is o(nlogn) for sorting
# space compelxity = 1

arr = [5,1,0,3,8,3,5]
n=len(arr)
a= arr.sort()
print(arr[n-1])


#optimal way:
#time complexity is o(n)
arr=[1,2,3,3,5]
n=len(arr)
def find_largest():
    largest=arr[0]
    for i in range(0,n):
        if arr[i]>largest:
            largest=arr[i]
    print(largest)
find_largest()

