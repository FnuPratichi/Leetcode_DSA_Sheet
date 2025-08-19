class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self,x):
        self.stack.append(x)
    
    def isEmpty(self):
        if len(self.stack) == 0:
            print("stack is empty")
            return None
    
    def remove(self):
        if self.isEmpty():
            print("stack is empty, nothing can't be reomved")
            return None
        return self.stack.pop()
    
    def top(self):
        if self.isEmpty():
            print("stack is empty , top is -1")
            return None
        return self.stack[-1]
    
    def Size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

s = Stack()
s.push(6)
s.push(7)
s.push(8)
s.push(9)
print(s)
print(s.remove())
print(s)  
print(s.remove())
print(s)
print("Size:", s.Size())
print("Top:", s.top())
    