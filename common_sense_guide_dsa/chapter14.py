"""
Chapter 14 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""
class Node:
    def __init__(self, next=None, value=None):
        self.next = next
        self.value = value
    
    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value
    
    def set_next(self, next):
        self.next = next
    
    def set_value(self, value):
        self.value = value

    def delete_node(self):
        self.value = self.next.value
        self.next = self.next.next
    
class LinkedList():
    def __init__(self, node=None):
        self.node = node
    
    def get(self, index):
        current_node = self.node
        for i in range(index + 1):
            current_node = current_node.next
        return current_node

    def set(self, index, value):
        current_node = self.node
        for i in range(index + 1):
            current_node = current_node.next
        current_node.value = value
    
    def print(self):
        node = self.node
        while node is not None:
            print(node.value)
            node = node.next
    
    def return_last(self):
        node = self.node
        while node.next is not None:
            node = node.next
        return node.value

    def reverse(self):
        previous = None
        node = self.node
        next = self.node.next
        while True:
            node.next = previous
            if next is None:
                break
            previous = node
            node = next
            next = node.next

        self.node = node



class DoubleNode:
    def __init__(self, last=None, next=None, value=None):
        self.last = last
        self.next = next
        self.value = value

    def get_last(self, last):
        return self.last

    def get_next(self):
        return self.next
    
    def get_value(self):
        return self.value

    def set_last(self, last):
        self.last = last

    def set_next(self, next):
        self.next = next
    
    def set_value(self, value):
        self.value = value
    

class DoubleLinkedList():
    def __init__(self, first=None, last=None):
        self.first = first
        self.last = last
    
    def get(self, index):
        current_node = self.node
        for i in range(index + 1):
            current_node = current_node.next
        return current_node

    def set(self, index, value):
        current_node = self.node
        for i in range(index + 1):
            current_node = current_node.next
        current_node.value = value
    
    def print_reverse(self):
        node = self.last
        while node is not None:
            print(node.value)
            node = node.last

def main():
    print("Testing")
    node5 = Node(value=4)
    node4 = Node(value=10, next=node5)
    node3 = Node(value=0, next=node4)
    node2 = Node(value=7, next=node3)
    node1 = Node(value=3, next=node2)
    linked_list = LinkedList(node=node1)
    print("LinkedList printed:")
    linked_list.print()

    dnode5 = DoubleNode(value=4)
    dnode4 = DoubleNode(value=10, next=dnode5)
    dnode3 = DoubleNode(value=0, next=dnode4)
    dnode2 = DoubleNode(value=7, next=dnode3)
    dnode1 = DoubleNode(value=3, next=dnode2)
    dnode5.set_last(dnode4)
    dnode4.set_last(dnode3)
    dnode3.set_last(dnode2)
    dnode2.set_last(dnode1)
    double_linked_list = DoubleLinkedList(first=dnode1, last=dnode5)
    print("Doubly LinkedList printed in Reverse Order:")
    double_linked_list.print_reverse()

    print("Last Value:")
    print(linked_list.return_last())

    print("Reverse LinkedList:")
    linked_list.reverse()
    linked_list.print()

    print("Delete middle node")
    node3.delete_node()
    linked_list.print()

main()