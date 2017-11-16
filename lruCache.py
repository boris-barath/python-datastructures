class Node(object):
    """
    LRU Cache node which keeps track of key, value, previous and next nodes
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

    def setNext(self, node):
        self.next = node

    def setPrev(self, node):
        self.prev = node

class LRUCache(object):
    """
    LRU Cache implementation in python
        - cache can be initialized with a fixed size: LRUCache(size)
        - most recent item is at the end of the linked list
        - if cache is full, remove least recently used element
    """
    def __init__(self, size):
        self.size = size
        self.map = {}
        self.head = Node(0, "Head")
        self.tail = Node(0, "Tail")
        self.head.setNext(self.tail)
        self.tail.setPrev(self.head)

    def __str__(self):
        string = []
        for node in self.map.values():
            string.append([node.key, node.value])
        return str(string)

    def get(self, key):
        if key not in self.map:
            return -1
        else:
            n = self.map[key]
            return n.value

    def insert(self, key, value):
        n = Node(key, value)
        if key in self.map:
            oldnode = self.map[key]
            self._del(oldnode)
            self.map[key] = n
        else:
            self._add(n)
            self.map[key] = n
            if (len(self.map)) > self.size:
                oldnode = self.head.next
                del self.map[oldnode.key]
                self._del(oldnode)
                del oldnode

    def _del(self, node):
        node.prev.setNext(node.next)
        node.next.setPrev(node.prev)

    def _add(self, node):
        node.setNext(self.tail)
        node.setPrev(self.tail.prev)
        self.tail.prev.setNext(node)
        self.tail.setPrev(node)

c = LRUCache(2)

c.insert(1, "Hello")
print(c.get(1))
c.insert(2, "Hiya")
print(c.get(2))
c.insert(3, "Haii")
print(c.get(3))
print(c.get(1))
print(c)
