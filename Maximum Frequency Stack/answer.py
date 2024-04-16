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
class FreqStack:

    def __init__(self):
        self.head=Stack()

    def push(self, val: int) -> None:
        """
        Pushes the given value onto the head of the stack.

        Parameters:
            val (int): The value to be pushed onto the stack.

        Returns:
            None
        """
        self.head.push(val)

    def pop(self) -> int:
        """
        A function that pops and returns the most frequent element from the head of the deque.
        This function does not take any parameters.
        It returns the most frequent element as an integer.
        """
        counts = {}
        c_n = self.head.head
        while c_n:
            counts[c_n.val] = counts.get(c_n.val, 0) + 1
            c_n = c_n.next
        max_count = max(counts.values())
        c_n = self.head.head
        while c_n:
            if c_n.next:
                if counts[c_n.val] == max_count:
                    i = c_n.val
                    c_n.val = c_n.next.val
                    c_n.next = c_n.next.next
                    return i
            c_n = c_n.next
        return self.head.pop()
