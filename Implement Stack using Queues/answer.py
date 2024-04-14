"""f"""
class Node:
    """d"""
    def __init__(self, val=None,next1=None):
        self.val = val
        self.next = next1
class Queue:
    """D"""
    def __init__(self):
        self.head = Node()
    def __len__(self):
        """
        A function that returns the number of nodes in the linked list.
        """
        c_n=self.head
        i=0
        while c_n:
            c_n=c_n.next
            i+=1
        return i
    def append(self, x: int) -> None:
        """
        A function that inserts a new node with a given value at the end of the linked list.
        
        Parameters:
            x (int): The value to be inserted.
        
        Returns:
            None
        """
        if self.head.val is None:
            self.head.val=x
        else:
            c_n=self.head
            while c_n.next:
                c_n=c_n.next
            c_n.next=Node(x)
    def pop(self) -> int:
        """
        A function that removes and returns the value of the node at the beginning of the linked list.
        
        :return: int - the value of the node at the beginning of the linked list
        """
        c_n=self.head
        if c_n.next:
            self.head=c_n.next
        else:
            self.head=Node()
        return c_n.val
    def peek(self) -> int:
        """
        A function that returns the value of the node at the beginning of the linked list without removing it.
        
        :return: int - the value of the node at the beginning of the linked list
        """
        return self.head.val
    def empty(self) -> bool:
        """
        A function that checks if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head is None or self.head.val is None
class MyStack:
    """d"""
    def __init__(self):
        self.head = Queue()
    def push(self, x: int) -> None:
        """
        A function that inserts a new node with a given value at the end of the linked list.
        
        Parameters:
            x (int): The value to be inserted.
        
        Returns:
            None
        """
        new_q = Queue()
        while not self.head.empty():
            new_q.append(self.head.pop())
        new_q.append(x)
        while not new_q.empty():
            self.head.append(new_q.pop())
    def __repr__(self) -> str:
        return str(self.head)
    def pop(self) -> int:
        """
        A function that removes and returns the value of the node at the beginning of the linked list.
        
        :return: int - the value of the node at the beginning of the linked list
        """
        new_q = Queue()
        for _ in range(len(self.head) - 1):
            new_q.append(self.head.pop())
        l=self.head.pop()
        while not new_q.empty():
            self.head.append(new_q.pop())
        return l
    def top(self) -> int:
        """
        A function that returns the value of the node at the beginning of the linked list without removing it.
        
        :return: int - the value of the node at the beginning of the linked list
        """
        new_q = Queue()
        for _ in range(len(self.head) - 1):
            new_q.append(self.head.pop())
        l=self.head.pop()
        while not new_q.empty():
            self.head.append(new_q.pop())
        self.head.append(l)
        return l
    def empty(self) -> bool:
        """
        A function that checks if the linked list is empty.

        Returns:
            bool: True if the linked list is empty, False otherwise.
        """
        return self.head.empty()
