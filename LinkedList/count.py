name = "PPatichi"
my_dict = {}

for i in range(0,len(name)):
    if name[i] not in my_dict:
        my_dict[name[i]] = 1 
    else:
         my_dict[name[i]]+=1
print(my_dict)


# MY_DICT[P], 1

class Node:
    def __init__(self,data):
        self.x = data
        self.next = None

f1 =  Node(5)
f2 = Node(6)
f1.next = f2

#head = Node(5, Node(6, Node(7, None)))

def traverseLL(head):
    temp  = head
    while(temp):
        print(temp.x)
        temp = temp.next

#traverseLL(f1)


arr = [1,2,3,4,5, "hello"]
head = Node(arr[0])
curr = head
for i in range(1,len(arr)):
    curr.next = Node(arr[i])
    curr = curr.next

traverseLL(head)


# f1 = Node(arr[0])
# f2 = Node(arr[1])
# f3 = Node(arr[2])
# f4 = Node(arr[3])
# f5 = Node(arr[4])
# f1.next = f2
# f2.next = f3
# f3.next = f4
# f4.next = f5
#traverseLL(f1)




