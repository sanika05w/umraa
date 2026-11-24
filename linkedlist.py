class node:
    def __init__(self ,data):
        self.data = data
        self.next = None
a = node (3)
b = node (4)
c = node (5)
d = node(None)

a.next = b
b.next = c
c.next = d
d.data = None
d.next = None

head = a 
print(head.data)
print(head.next.data)
print(head.next.next.data)

#traverse the node 

def printlinkedlist(head):
    curr = head
        
    while curr != None and curr.data != None :
       print(curr.data , end = " ")
       curr = curr.next
printlinkedlist(head)

