#brute force way 
arr = [8,5,1,0,2,7,7]
n=len(arr)
arr.sort()
largest=arr[n-1]
for i in range(n-2,-1,-1):  #startung loop from n-2 index till 0 
    if arr[i]!=largest:
        second_largest= arr[i]
        break
print(second_largest)

# better way 

arr=[1,2,4,7,7,5]
arr.sort()
n=len(arr)
largest = arr[0]
for i in range(0,n):
    if arr[i]>largest:
        largest=arr[i]
print(largest)

second_largest=-1
for i in range(0,n):
    if arr[i]>second_largest and arr[i]!=largest:
        second_largest=arr[i]
print(second_largest)



