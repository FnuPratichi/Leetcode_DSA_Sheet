#create nodes
class Node:
    def __init__(self,data):
        self.next = None
        self.data = data

# create nodes , first = [data,None] , second = [data,none], third = [data,none]
first = Node(5) 
second = Node(10)
third = Node(15)

#Link them, head-->>first [5,first.next] -->second[10,third.next]-->third[15,null]
first.next = second  
second.next = third


#Head track
head = first

#Traverse & print
current = head
while current:
    print(current.data)
    current = current.next



