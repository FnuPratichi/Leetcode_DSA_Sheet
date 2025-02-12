# count the occurance of numbers in list 
# Brute force way
"""numbers = [1,2,3,1,1,0]
count=0
target  = int(input())
length = len(numbers)
for i in range(0,length):
    if numbers[i]==target:
        count=count+1
print(count)"""

# hashing technique 
number_list = []
n = int(input("Enter the nukber of elemenst you want in your list "))
for i in range(n):
    num = int(input())
    number_list.append(num)
print(number_list)

query_list = []
q = int(input("Enter no of query "))
for j in range(q):
    query = int(input())
    query_list.append(query)
print(query_list)


# precompute 
hash = [0] * 12   # initiazed by zero and of size 12
for i in range(n):
    hash[number_list[i]]+=1
print(hash)



