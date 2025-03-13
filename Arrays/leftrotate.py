# ouptut should be = arr [2,3,4,5,1]
# left rotate array by one place
arr = [1,2,3,4,5]
def rotate_left(arr):
    temp = arr[0]
    n = len(arr)
    for i in range(1,n):
        arr[i-1] = arr[i]
    arr[n-1] = temp


if __name__ == "__main__":
    rotate_left(arr)
    print(arr)


