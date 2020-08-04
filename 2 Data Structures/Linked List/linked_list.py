# Linked list example

# The node class

class Node(object):
    # class stores a single data field called val
    # next indicate this is a singly linked list
    def __init__(self, val):
        self.val = val
        self.next = None

    def get_data(self):
        return self.val
    
    def set_data(self, val):
        self.val = val

    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next


# the LinkedList class
class LinkedList(object):
    def __init__(self, head=None):
        
