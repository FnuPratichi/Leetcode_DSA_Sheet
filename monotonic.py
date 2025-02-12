def monotonic_fun(arr):
    increasing = True
    decreasing = True
    for i in range(0,len(arr)-1):
        if arr[i] < arr[i+1]:
            decreasing = False
        elif arr[i] > arr[i+1]:
            increasing = False
    if increasing:
        print("increasing")
    elif decreasing:
        print("decreasing")
    else:
        print("neither")
    

arr1 = [1,2,0,3,4]
arr2 = [1,2,2,3]
arr3 = [6,5,4,3,2,1]
arr4 = [1,2,0,1,0]
monotonic_fun(arr1)
monotonic_fun(arr2)
monotonic_fun(arr3)
monotonic_fun(arr4)


        

        
    