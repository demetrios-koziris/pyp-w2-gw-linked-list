from .interface import AbstractLinkedList
from .node import Node
from functools import reduce

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=[]):
        self.start = None
        self.end = None
        for elem in elements:
            self.append(elem)

    def __str__(self):
        return str([node.elem for node in self])

    def __len__(self):
        return reduce(lambda x,y: x+1, [node for node in self], 0)
                
    def __iter__(self):
        pointer = self.start
        while not pointer is None:
            yield pointer
            pointer = pointer.next
        raise StopIteration()

    def __getitem__(self, index):
        if index < 0 or index > len(self)-1:
            raise IndexError("Index out of Range")
        for i, node in enumerate(self):
            if i == index:
                return node
            
    def __add__(self, other):
        new_ll = LinkedList()
        for node in self:
            new_ll.append(node.elem)
        for node in other:
            new_ll.append(node.elem)
        return new_ll

    def __iadd__(self, other):
        for node in other:
            self.append(node.elem)
        return self

    def __eq__(self, other):
        if len(self) != len(other):
            return False
        return not False in [node1 == node2 for node1, node2 in zip(self, other)]

    def __ne__(self, other):
        return not self == other
        
    def append(self, elem):
        new_node = Node(elem) 
        if len(self) == 0:
            self.start = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = self.end.next

    def count(self):
        return len(self)

    def pop(self, index=None):
        # default index should be the end node
        if index is None:
            index = len(self)-1
        popped_node = self[index]
        if len(self) == 1:
            self.start = None
            self.end = None
        elif popped_node is self.start:
            self.start = popped_node.next
        else:
            if popped_node is self.end:
                self.end = self[index-1]
            self[index-1].next = popped_node.next
        return popped_node.elem