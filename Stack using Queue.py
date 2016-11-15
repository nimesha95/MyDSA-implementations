class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.size=0
        self.head=None

    def enqueue(self,data):
        newNode=Node(data)
        if (self.head==None):
            self.head=newNode
            self.size +=1
        else:
            curNode=self.head
            while curNode.next:
                curNode=curNode.next
            curNode.next=newNode
            self.size += 1

    def dequeue(self):
        curNode=self.head
        self.head=curNode.next
        curNode.next=None
        self.size -= 1
        return curNode.data
        #print(curNode.data,"dequeued")

    def size(self):
        return self.size

class Stack:
    def __init__(self):
        self.q1=Queue()
        self.q2=Queue()

    def push(self,data):
        self.q1.enqueue(data)

    def pop(self):
        while (not self.q1.size==1):
            x=self.q1.dequeue()
            self.q2.enqueue(x)
        z=self.q1.dequeue()
        while (not self.q2.size==0):
            y=self.q2.dequeue()
            self.q1.enqueue(y)
        return z

    def peek(self):
        while (not self.q1.size==1):
            x=self.q1.dequeue()
            self.q2.enqueue(x)
        z=self.q1.dequeue()
        self.q2.enqueue(z)
        while (not self.q2.size==0):
            y=self.q2.dequeue()
            self.q1.enqueue(y)
        return z

    def isEmpty(self):
        if self.q1.size==0:
            print("Yes")
            return True
        else:
            print("No")
            return False

    def size(self):
        return self.q1.size

s=Stack()
s.push(5)
s.push(6)
s.pop()
#print(s.peek())
s.push(10)
#print(s.peek())
#print(s.pop())
print(s.size())
s.pop()
s.pop()
s.isEmpty()

