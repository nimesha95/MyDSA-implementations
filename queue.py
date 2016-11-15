class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class queue:
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
        print(curNode.data,"dequeued")


q=queue()
q.enqueue(7)
q.enqueue(8)
print(q.size)
q.dequeue()
#print(q.size)
q.enqueue(10)
q.enqueue(15)
q.dequeue()
print(q.size)