from heapq import heappush, heappop, heappushpop, heapify, _heapify_max

"""
Implements a priority logger with fixed size
    -implemented using a minHeap
    - can initialise with fixed size Logger(capacity)
    - add log tuple (priority, message)
    - if log is full, remove message with lowest priority then insert
    - can list all messages in O(n) with getMessages
    - getOrderedMessages is not recommended unless you need
      since the array has to be re-ordered twice.
"""

class Logger(object):
    def __init__(self, capacity):
        """
        Initialise with capacity of logs
        """
        self.mh = []
        self.capacity = capacity

    def log(self, (priority, message)):
        """
        Add new message with priority to log,
        if priority is less than lowest priority,
        ignore the message
        """
        if len(self.mh) >= self.capacity:
            p, m = self.showMin()
            if p > priority:
                return
            self.deleteMin()
        heappush(self.mh, (priority, message))

    def showMin(self):
        """
        Show lowest priority element in the log
        """
        return self.mh[0]

    def deleteMin(self):
        """
        Delete lowest priority element in the log
        """
        heappop(self.mh)

    def getMessages(self):
        """
        Return all messages in the log
        """
        msgs = []
        for x in range(len(self.mh)):
            val, msg = self.mh[x]
            msgs.append(msg)
        return msgs

    def getOrderedMessages(self):
        """
        Return all messages with highest priority messages first
        """
        _heapify_max(self.mh)
        res = self.getMessages()
        heapify(self.mh)
        return res

l = Logger(2)
l.log((15, "Syntax Error"))
l.log((100000, "CORE MELTDOWN"))
l.log((5, "Fart"))
print(l.getMessages())
print(l.getOrderedMessages())
