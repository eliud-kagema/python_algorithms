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
        self.head = head
        self.count = 0

    def get_count(self):
        return self.count

    def insert(self, data):
        # TODO: insert a new node
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
        self.count += 1

    def find(self, val):
        # TODO: find the first item with the given value
        item = self.head
        while(item != None):
            if item.get_data() == val:
                return item
            else:
                item = item.get_next()

        return None

    def deleteAt(self, idx):
        # TODO: delete an item at given index
        if idx > self.count-1:
            return
    
    def dump_list(self):
        tempnode = self.head
        while (tempnode != None):
            print("Node: ", tempnode.get_data())
            tempnode = tempnode.get_next()


# Create a linked list and insert some items

itemList = LinkedList()
itemList.insert(38)
itemList.insert(49)
itemList.insert(13)
itemList.insert(15)
itemList.dump_list()

# Exercise the list
print("Item count: ", itemList.get_count())
print("Finding an item: ", itemList.find(13))
print("Finding an item: ", itemList.find(73))