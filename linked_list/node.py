class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        return str(self.elem)

    def __eq__(self, other):
        
        #if self.elem is not None and other.elem is not None:
        if type(other) is Node:
            return self.elem == other.elem
        else:
            return self.elem == other

    def __repr__(self):
        return str(self.elem)
