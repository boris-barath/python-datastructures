class Node(object):
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.prev = None

class LinkedList(object):
    """
    LinkedList
        - can be used as a stack - using append and peek and pop
        - print with printList()
    """
    def __init__(self):
        self.head = Node("Head")
        self.tail = Node("Tail")
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, elem):
        n = Node(elem)
        n.prev = self.tail.prev
        n.prev.next = n
        n.next = self.tail
        self.tail.prev = n

    def peek(self):
        return self.tail.prev.value

    def pop(self):
        n = self.tail.prev
        v = n.value
        n.prev.next = self.tail
        self.tail.prev = n.prev
        del n
        return v

    def get(self, index):
        cur = self.head.next
        i = 0
        while cur is not self.tail:
            if index == i:
                return cur.value
            else:
                i += 1
                cur = cur.next
        print("Error - Index out of bounds")

    def printList(self):
        cur = self.head.next
        while cur is not self.tail:
            print(cur.value)
            cur = cur.next

    def insert(self, index, value):
        #TODO: implement index-wise inserting
        print("Implement insert")

l = LinkedList()

l.append(10)

l.printList()
