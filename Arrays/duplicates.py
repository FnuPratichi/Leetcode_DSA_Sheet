#Brute way 
# note that insertion in set take o(1) TC in best case and o(n) in worst case
nums = [1,1,2,2,2,3,3,4]

def remove_dup():
    unique_value = set(nums)
    print(unique_value)
    #print(len(unique_value))
    index=0
    l = list(unique_value)
    a=len(l)
    for i in range(0,a):
        nums[index]=i
        index=index+1
    print(index)
remove_dup()


# using 2 pointer approach 
nums = [1,1,2,2,2,3,3]
def remove_duplicates():
    i=0
    for j in range(1,len(nums)):
        if nums[j]!=nums[i]:
            nums[i+1]=nums[j]
            i=i+1
    print(i+1)
remove_duplicates()
