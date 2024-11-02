

class Deque():

    def __init__(self, size):
        self.list = [None] * size
        self.frontpointer = 0
        self.rearpointer = 0
        self.length = 0
        self.size = size

    def append(self, x):
        self.list[self.frontpointer] = x
        self.frontpointer = (self.frontpointer + 1) % self.size
        self.length += 1

    def appendleft(self, x):
        self.rearpointer = (self.rearpointer - 1) % self.size
        self.list[self.rearpointer] = x
        self.length += 1

    def pop(self):
        self.frontpointer = (self.frontpointer - 1) % self.size
        dummy = self.list[self.frontpointer]
        self.list[self.frontpointer] = None
        self.length -= 1
        return dummy
    

    def popleft(self):
        dummy = self.list[self.rearpointer]
        self.list[self.rearpointer] = None
        self.rearpointer = (self.rearpointer + 1) % self.size
        self.length -= 1
        return dummy

    def peek(self):
        return self.list[self.frontpointer - 1]

    def peekleft(self):
        return self.list[self.rearpointer]

    def __len__(self):
        return self.length

    def __iter__(self):
        return DequeIterator(self)

    def __getitem__(self, n):
        return self.list[(self.rearpointer + n) % self.size]


class DequeIterator:

    def __init__(self, deque):
        self.index = 0
        self.deque = deque

    def __iter__(self):
        return self

    def __next__(self):
        if (self.index >= len(self.deque)):
            raise StopIteration
        self.index += 1
        return self.deque[self.index-1]
