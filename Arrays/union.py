arr1 = [1,1,2,3,4,5]
arr2 = [2,3,4,4,5]

def find_union(arr1,arr2):
    union_dict = {}
    for i in range(0,len(arr1)):
        if arr1[i] not in union_dict:
            union_dict[arr1[i]] = arr1[i]
    for i in range(0,len(arr2)):
        if arr2[i] not in union_dict:
            union_dict[arr2[i]] = arr2[i]
    print(union_dict) 

    union = []
    for keys in union_dict:
        union.append(keys)
    print(union)

    

            





find_union(arr1,arr2)
