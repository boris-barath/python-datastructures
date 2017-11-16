from heapq import heappush, heappop, heappushpop, heapify

    '''
    MinHeap:
        - construct with size only or with size and array
        - MinHeap(size) or MinHeap(size, array)
        - Insert elements with insert(elem)
        - Peek min element with peek()
        - Remove and return minimal element with getMin()
    '''

class MinHeap(object):
    '''
    Can either take values (ints) or pairs of (int, object)
    '''
    def __init__(self, size, array = None):
        self.size = size
        self.arr = []
        if array is not None:
            heapify(array)
            self.arr = array

    def insert(self, elem):
        '''
        This way of inserting does not insert into full arr
        '''
        if len(self.arr) == self.size:
            return
        else:
            heappush(self.arr, elem)

    def getMin(self):
        '''
        Removes and returns min
        '''
        return heappop(self.arr)

    def peek(self):
        '''
        Returns min but does not remove it
        '''
        return self.arr[0]
