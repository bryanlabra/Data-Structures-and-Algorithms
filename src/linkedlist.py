class Node:
    def __init__(self, value=None, next=None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev
    
class LinkedList:
    def __init__(self):
        self.head = None
        #self.tail = None

    def insert(self):
        pass
    
    def delete():
        pass

n1 = Node(3)
n2 = Node(7)
n3 = Node(2)
n4 = Node(9)

LL = LinkedList()
LL.head = n1

n1.next = n2 #or LL.head.next
n2.next = n3 # or LL.head.next.next
n3.next = n4
#LL.tail = n4
