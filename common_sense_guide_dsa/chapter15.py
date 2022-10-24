"""
Chapter 15 exercises of "A Common-Sense Guide to Data Structures and Algorithms"
"""


class TreeNode:
    def __init__(self, value, left_node=None, right_node=None):
        self.value = value
        self.left_node = left_node
        self.right_node = right_node

def construct_tree():
    node10 = TreeNode(77)
    node9 = TreeNode(80, left_node=node10)
    node8 = TreeNode(60)
    node7 = TreeNode(75, left_node=node8, right_node=node9)
    node6 = TreeNode(47)
    node5 = TreeNode(33)
    node4 = TreeNode(10)
    node3 = TreeNode(35, left_node=node5, right_node=node6)
    node2 = TreeNode(25, left_node=node4, right_node=node3)
    node1 = TreeNode(50, left_node=node2, right_node=node7)
    return node1

def find_greatest_tree_value(tree):
    if tree.right_node is None:
        return tree.value
    return find_greatest_tree_value(tree.right_node)

def main():
    print("Testing")
    tree = construct_tree()
    print(find_greatest_tree_value(tree))

main()