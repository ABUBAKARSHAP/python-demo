class Node:
    def __init__(self, e) -> None:
        self.data = e
        self.per = None
        self.next = None
class CircularLinklist:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0
    def insertAtfirst(self, e):
        n = Node(e)
        
        if self.head == None:
            self.head = n
            self.tail = n
            self.head.per = self.tail
            self.tail.next  = self.head
            self.count =1
        else:
            n.next = self.head
            self.head.per = n
            self.head = n
            self.head.per = self.tail
            self.count +=1

    def show(self):
        x = self.head
        while x != self.tail.next:
            print(x.data)
            x = x.next
s = CircularLinklist()
s.insertAtfirst(3)
s.insertAtfirst(234)
s.insertAtfirst(34)
s.show()
print(s.tail.data) # 3
print(s.head.per.data) # 34
