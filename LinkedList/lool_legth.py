# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None


class Solution:
    def countNodesInLoop(self, head):
        temp = head
        my_dict = {}
        timer = 1
        while(temp):
            if temp not in my_dict:
                my_dict[temp] = timer
                temp = temp.next
                timer = timer+1

            length = timer - my_dict[temp]
            print(length)
            print(timer)