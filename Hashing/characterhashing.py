# case1 : when you know that string has only lowercases
# ASCII value of a-z is 97-122 , so max value cpuld be 25(122-97)

number_list = []
n =  int(input("enter the size of list"))
for i in range(n):
    c = input("enter characters in list ")
    number_list.append(c)
print(number_list)

hash = [0]*25
for i in range(n):
    hash[ord(number_list[i])-ord('a')]+=1


query_list = []
q = int(input("size of the query"))
for j in range(q):
    ch = input("enter the char ")
    query_list.append(ch)

for ch in query_list:
    print(hash[ord(ch)-ord('a')])

