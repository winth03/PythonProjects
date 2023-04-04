class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass

class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return True if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Error attempting to access an element from an empty container.')
        return self._data[self._front]
        
    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).

        Raise Empty exception if the queue is empty.
        """
        if self.is_empty():
            raise Empty('Error attempting to access an element from an empty container.')
        e = self._data[self._front]
        self._data[self._front] = None
        self._front += 1
        self._size -= 1
        return e

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._front + len(self) == len(self._data) - 1:
            self._resize(len(self._data) * 2)
        self._data[self._front + len(self)] = e
        self._size += 1

    def _resize(self, cap):                     # we assume cap >= len(self)
        """Resize to a new list of capacity >= len(self)."""
        temp = [None] * cap
        for i in range(len(self._data)):
            temp[i] = self._data[i]
        self._data = temp


class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__(self):
        """Create an empty stack."""
        self._data = []

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self._data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self._data.append(e)

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
        
    def pop(self, i=-1):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop(i)

class ArrayDeque():
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size
        
    def is_empty(self):
        return len(self) == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]
    
    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[(self._front + self._size - 1) % len(self._data)]

    def add_first(self, value):
        # resize
        if len(self) == len(self._data):
            self._resize(len(self._data) * 2)
        # add value to first element of queue
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = value
        self._size += 1

    def add_last(self, value):
        # resize
        if len(self) == len(self._data):
            self._resize(len(self._data) * 2)
        # add value to last element of queue
        back = (self._front + self._size) % len(self._data)
        self._data[back] = value
        self._size += 1
        
    def delete_first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        e = self._data[self._front]
        self._data[self._front] = None
        self._size -= 1
        self._front = (self._front + 1) % len(self._data)
        return e

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        back = (self._front + self._size - 1) % len(self._data)
        e = self._data[back]
        self._data[back] = None
        self._size -= 1
        return e

    def _resize(self, capacity):
        temp = [None] * capacity
        for i in range(len(self)):
            index = (self._front + i) % len(temp)
            temp[i] = self._data[index]
        self._data = temp
        self._front = capacity
