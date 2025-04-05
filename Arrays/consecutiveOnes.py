arr1 = [1,1,0,1,1,1,0,1,1]

def max_consecutiveOnes(arr1):
    count = 0
    count_list = []
    
    for i in range(0,len(arr1)):
        if arr1[i]!=1:
            count_list.append(count)
            count = 0
        else:
            count = count+1
    return max(count_list)
            

