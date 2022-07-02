"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from datetime import datetime

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.next_node = None

class LinkedList:
    def __init__(self, head_node):
        self.head_node = head_node

    def listprint(self):
        printval = self.head_node
        while printval is not None:
            if printval.next_node is not None:
                print(str(printval.dataval) + "->", end = "")
            else:
                print(str(printval.dataval))
            printval = printval.next_node

def merge_linked_lists(list_one, list_two):
    result = LinkedList(Node())
    head_one = list_one.head_node
    next_one = head_one
    head_two = list_two.head_node
    next_two = head_two
    current_node = Node()
    if head_one.dataval <= head_two.dataval:
        result.head_node = head_one
        current_node = head_one
        next_one = head_one.next_node
    else:
        current_node = head_two
        next_two = head_two.next_node
    while True:      
        if next_two is None or next_one is not None and next_one.dataval <= next_two.dataval:
            current_node.next_node = next_one
            next_one = next_one.next_node
        else:
            current_node.next_node = next_two
            next_two = next_two.next_node
        current_node = current_node.next_node
        if next_one is None and next_two is None:
            break
    
    return result

def generate_linked_lists():
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(4)
    node1.next_node = node2
    node2.next_node = node3

    node4 = Node(1)
    node5 = Node(3)
    node6 = Node(4)
    node4.next_node = node5
    node5.next_node = node6

    return LinkedList(node1), LinkedList(node4)


def main():
    start_time = datetime.now()

    list1, list2 = generate_linked_lists()
    print("Before:")
    list1.listprint()
    list2.listprint()

    print("After:")
    list3 = merge_linked_lists(list1, list2)
    list3.listprint()
    finish_time = datetime.now()
    print("Runtime: " + str(finish_time - start_time))

main()

