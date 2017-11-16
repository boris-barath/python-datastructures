from heapq import heappush, heappop, heappushpop, heapify

class Logger(object):
    def __init__(self, capacity):
        self.mh = []
        self.capacity = capacity

    def insert(self, (priority, message)):
        heappush(self.mh, (priority, message))
        if len(self.mh) > self.capacity:
            
