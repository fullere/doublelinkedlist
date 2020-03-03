# Elizabeth Fuller
# 3/2/20
# Double Linked List Class


class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

    def __repr__(self):
        return repr(self.data)


class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def add_to_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if self.tail == None:
            self.tail = new_node

    def push_end(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.head.prev = None
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
        new_node.prev = curr
        self.tail = new_node

    def pop_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def pop_end(self):
        current = self.head
        previous = self.head
        while current.next:
            previous = current
            current = current.next
        previous.next = None
        return current.data
