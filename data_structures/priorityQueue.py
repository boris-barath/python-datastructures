from minHeap import *

class PriorityQueue(object):
    def __init__(self, size):
        self.size = size
        self.mh = MinHeap(size)

    def enqueue(self, priority, item):
        self.mh.insert((-priority, item))

    def dequeue(self):
        priority, item = self.mh.getMin()
        return (-priority, item)

    def peek(self):
        priority, item = self.mh.peek()
        return (-priority, item)

pq = PriorityQueue(2)
pq.enqueue(4, '1')
pq.enqueue(3, 'a')
pq.dequeue()
pq.enqueue(1, 'a')
print(pq.mh.arr)
