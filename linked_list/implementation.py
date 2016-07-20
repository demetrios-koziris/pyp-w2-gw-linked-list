from .interface import AbstractLinkedList
from .node import Node
from functools import reduce

class LinkedList(AbstractLinkedList):
    """
    Implementation of an AbstractLinkedList inteface.
    """

    def __init__(self, elements=[]):
        #self.elements = elements
        self.start = None
        self.end = None
        for elem in elements:
            self.append(elem)

    def __str__(self):
        return_string = "["
        for node in self:
            return_string += str(node)
            if not node is self.end:
                return_string += ", "
        return_string += "]"
        return return_string

    def __len__(self):
        return reduce(lambda x,y: x+1, [node for node in self], 0)
                
    def __iter__(self):
        if self.start is None:
            raise StopIteration()
        else:
            pointer = self.start
            while not pointer is self.end:
                yield pointer
                pointer = pointer.next
            yield pointer
            raise StopIteration()

    def __getitem__(self, index):
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
        '''Must be another node'''
        new_ll = LinkedList()
        for node in self:
            new_ll.append(node.elem)
        for node in other:
            new_ll.append(node.elem)
        return new_ll

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
        if index is None:
            index = len(self)-1
        if index < 0 or index > len(self)-1:
            raise IndexError("Index out of Range")
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
        return popped_node