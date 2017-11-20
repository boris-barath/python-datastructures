class Stack(object):
    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.size = -1
        self.arr = []

    def __str__(self):
        return str(self.arr[0:self.size + 1])

    def push(self, val):
        if self.size == self.maxsize - 1:
            print("Error - Stack is full")
            return
        self.arr.append(val)
        self.size += 1

    def pop(self):
        if self.size == -1:
            print("Error - Stack is empty")
            return
        self.size -= 1
        return self.arr[self.size]


    def peek(self):
        if self.size == 0:
            print("Error - Stack is empty")
            return
        return self.arr[self.size]
