# arr =  [0,1,2,4,5]
# N = len(arr)
# for i in range(0,N+1):
#     if i not in arr:
#         print(i)

# TC = O(N)*O(N) 
# SC = O(1) no extra space used

#Better way 
my_dict = {}
arr1 =  [0,1,2,3,5]

for i in range(0,len(arr1) + 1):
    my_dict[i] = 0


for i in range(0,len(arr1)):
    my_dict[arr1[i]] = 1
    
for keys,values in my_dict.items():
    if values==0:
        print(keys)




