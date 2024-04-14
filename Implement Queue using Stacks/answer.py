"""f"""
class Node:
    """D"""
    def __init__(self, val=None,next1=None):
        self.val = val
        self.next = next1
class Stack:
    """D"""
    def __init__(self):
        self.head = Node()
    def is_empty(self):
        """
        Check if the value of the head node is None.
        """
        if not self.head:
            return True
        return self.head.val is None
    def push(self,n_w):
        """
        Add a new node to the top of the stack.
        """
        if self.is_empty():
            self.head=Node(n_w)
        else:
            n_n = Node(n_w)
            n_n.next = self.head
            self.head = n_n
    def pop(self):
        """
        Remove the node at the top of the stack.
        """
        if self.is_empty():
            return None
        n_n=self.head.val
        self.head=self.head.next
        return n_n
    def peek(self):
        """
        Return the value of the node at the top of the stack.
        """
        if not self.head or not self.head.is_empty():
            return None
        return self.head.val
    def __len__(self):
        """
        Return the number of nodes in the stack.
        """
        n_n = self.head
        i = 0
        while n_n is not None:
            n_n = n_n.next
            i += 1
        return i
    def __repr__(self) -> str:
        s=''
        cop=self.head
        while cop:
            s += str(cop.val) + '->'
            cop = cop.next
        return s
class MyQueue:
    """F"""
    def __init__(self):
        self.head = Stack()

    def push(self, x: int) -> None:
        """
        Pushes an integer onto the stack.
        
        Parameters:
            x (int): The integer to be pushed onto the stack.
        
        Returns:
            None
        """
        new_stack = Stack()
        while not self.head.is_empty():
            new_stack.push(self.head.pop())
        new_stack.push(x)
        while not new_stack.is_empty():
            self.head.push(new_stack.pop())
    def pop(self) -> int:
        """
        Method to remove and return the item at the head of the queue.
        
        :return: int - the item at the head of the queue
        """
        return self.head.pop()

    def peek(self) -> int:
        """
        Return the value at the top of the queue without removing it.
        """
        return self.head.peek()

    def empty(self) -> bool:
        """
        A function that checks if the 'head' attribute of the object is empty and returns a boolean value.
        This function does not take any parameters and returns a boolean value.
        """
        if self.head.is_empty():
            return True
        return False
