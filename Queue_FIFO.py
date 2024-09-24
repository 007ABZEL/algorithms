class Queue:
    """
    The Queue class implements a FIFO (first-in, first-out) queue.
    
    Methods:
        __init__(): Initializes the queue.
        enqueue(item): Adds an item to the queue.
        dequeue(): Removes and returns the front item from the queue.
        peek(): Returns the front item without removing it.
        is_empty(): Checks if the queue is empty.
        size(): Returns the size of the queue.
    """
    
    def __init__(self):
        """Initializes the queue."""
        self.queue = []

    def enqueue(self, item):
        """Adds an item to the queue.
        
        Args:
            item: The item to be added.
        """
        self.queue.append(item)

    def dequeue(self):
        """Removes and returns the front item from the queue.
        
        Returns:
            The front item of the queue. If the queue is empty, returns "Queue is empty".
        """
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            return "Queue is empty"

    def peek(self):
        """Returns the front item without removing it.
        
        Returns:
            The front item of the queue. If the queue is empty, returns "Queue is empty".
        """
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Queue is empty"

    def is_empty(self):
        """Checks if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.queue) == 0

    def size(self):
        """Returns the size of the queue.
        
        Returns:
            The number of items in the queue.
        """
        return len(self.queue)

queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.dequeue())
print(queue.peek())
print(queue.size())