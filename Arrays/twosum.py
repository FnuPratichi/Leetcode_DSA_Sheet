if __name__ == "__main__":
    arr = [2,6,5,8,11]
    target = 14

# def two_sum(arr,target):
#     for i in range(0,len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]+arr[j] == target:
#                 print(arr[i]+arr[j], "equal to target 14")
#                 print(i,j)
# two_sum(arr,target)


def two_sum(arr,target):
    my_dict = {}
    for i in range(0,len(arr)):
        b = target - arr[i]
        if b in my_dict:
            print([ my_dict[b],i])
        else:
            my_dict[arr[i]] = i
two_sum(arr,target)