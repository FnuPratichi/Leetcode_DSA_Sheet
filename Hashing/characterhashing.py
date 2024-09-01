# case1 : when you know that string has only lowercases
# ASCII value of a-z is 97-122 , so max value cpuld be 25(122-97)

"""number_list = []
n =  int(input("enter the size of list"))
for i in range(n):
    c = input("enter characters in list ")
    number_list.append(c)
print(number_list)

hash = [0]*26
for i in range(n):
    hash[ord(number_list[i])-ord('a')]+=1


query_list = []
q = int(input("size of the query"))
for j in range(q):
    ch = input("enter the char ")
    query_list.append(ch)

for ch in query_list:
    print(hash[ord(ch)-ord('a')])
"""

#case 2 : when you don't know the cases of string

string = []
n1 = int(input("size of string"))
for i in range(n1):
    c1 = input("enter your character ")
    string.append(c1)
print(string)

query = []
q1 = int(input("size of query string"))
for j in range(q1):
    ch1 = input("enter your character ")
    query.append(ch1)
print(query)

# pre compute 
hash = [0]* 256
for i in range(n1):
    hash[ord(string[i])]+=1

# fetching 
for ch1 in query:
    print(hash[ord(ch1)])