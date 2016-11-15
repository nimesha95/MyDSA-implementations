class Stack:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.insert(0,item)

    def pop(self):
        if self.isEmpty():
            return
            print("Can't pop from empty list")
        else:
            return self.stack.pop(0)

    def peek(self):
        print(self.stack[0])

    def isEmpty(self):
        if (len(self.stack)==0):
            #print("1")
            return True

        else:
            #print("2")
            return False

    def size(self):
        return len(self.stack)

s=Stack()
s.push(5)
s.push(6)
#print(s.size())
s.pop()
print(s.size())
s.isEmpty()
s.peek()

