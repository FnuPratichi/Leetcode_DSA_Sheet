if __name__ == "__main__":
    d = int(input())
    arr = [1,2,3,4,5,6,7]
    n = len(arr)


def d_rotate_left(arr,d,n):
    d = d%n
    #temp = nums[:k] 
    temp = []
    for i in range(0,d):
        temp.append(arr[i])
    print(temp)
    for i in range(d,n):
        arr[i-d] = arr[i]
    for i in range(n-d,n):
        arr[i] = temp[i-(n-d)]

d_rotate_left(arr,d,n)

print(arr)




