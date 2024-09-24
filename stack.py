class Stack:
    """
    A simple stack implementation.

    Attributes
    ----------
    stack : list
        The list to store stack elements.

    Methods
    -------
    push(item)
        Pushes an item onto the stack.
    pop()
        Removes and returns the top item of the stack.
    peek()
        Returns the top item of the stack without removing it.
    is_empty()
        Checks if the stack is empty.
    size()
        Returns the number of items in the stack.
    """

    def __init__(self):
        """
        Initializes an empty stack.
        """
        self.stack = []

    def push(self, item):
        """
        Pushes an item onto the stack.

        Parameters
        ----------
        item : any
            The item to be pushed onto the stack.
        """
        self.stack.append(item)

    def pop(self):
        """
        Removes and returns the top item of the stack.

        Returns
        -------
        any
            The top item of the stack if the stack is not empty.
        str
            "Stack is empty" if the stack is empty.
        """
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    def peek(self):
        """
        Returns the top item of the stack without removing it.

        Returns
        -------
        any
            The top item of the stack if the stack is not empty.
        str
            "Stack is empty" if the stack is empty.
        """
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    def is_empty(self):
        """
        Checks if the stack is empty.

        Returns
        -------
        bool
            True if the stack is empty, False otherwise.
        """
        return len(self.stack) == 0

    def size(self):
        """
        Returns the number of items in the stack.

        Returns
        -------
        int
            The number of items in the stack.
        """
        return len(self.stack)

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop()) 
print(stack.peek())
print(stack.size())
