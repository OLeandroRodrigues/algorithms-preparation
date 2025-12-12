"""
Problem: Insert a Value into an Existing Binary Search Tree

Statement:
    Given the root of an existing Binary Search Tree (BST) and a value,
    insert the value into the tree while preserving the BST property.

Constraints:
    - Number of nodes n ≥ 0
    - Values are comparable (integers for simplicity)
    - No duplicate values are inserted

Goal:
    Modify the existing tree by inserting the given value in the correct
    position according to BST ordering rules.

Approaches:
    - Version 1 (From Scratch):
        Implement the insertion logic manually, handling all base cases
        (empty tree, left insertion, right insertion).

Complexity Targets:
    - Time: O(h), where h is the height of the tree
        - Best case: O(log n) for balanced trees
        - Worst case: O(n) for skewed trees
    - Space:
        - O(h) using recursion
        - O(1) auxiliary space if implemented iteratively

How to run:
    pytest -q   # from the problems/ directory
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return Node(key) 
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        
        return node 

        


        