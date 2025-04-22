# BST-validity-checker
BST Implementation errors
An error in a BST implementation may result in a variety of problems. Ex: Key-related problems include:

A node X is in the left subtree of ancestor Y with X's key > Y's key
A node X is in the right subtree of ancestor Y with X's key < Y's key
Child-related problems include:

A node that is a child of two or more distinct nodes
A child attribute that references an ancestor
Examples of key-related problems:

Two binary trees, each with seven nodes. Left tree: Root's key is 40, root's left child has key 50, root's right child has key 80, node 50's left child has key 20, node 50's right child has key 60, node 80's left child has key 70, and node 80's right child has key 90. Node 50 is highlighted in red. Below the tree is the label: Key 50 (and 60) in 40's left subtree. Right tree: Root's key is 77, root's left child has key 44, root's right child has key 88, node 44's left child has key 33, node 44's right child has key 55, node 88's left child has key 66, and node 88's right child has key 99. Node 66 is highlighted in red. Below the tree is the label: Key 66 is 77's right subtree.

Examples of child-related problems:

Two binary trees, each with five nodes. Left tree: Root's key is 50, root's left child has key 25, root's right child has key 75, node 25's right child has key 37, and node 75's right child has key 88. A red arrow representing node 37's right child extends from node 37's lower right and points to node 75. A label below the left tree says: Node 75 is a child of two distinct nodes. Right tree: Root's key is 44, root's left child has key 22, root's right child has key 55, node 22's left child has key 11, and node 22's right child has key 33. A red arrow representing node 55's left child extends from node 55's lower left and points to node 44. A label below the left tree says: 55's left child is an ancestor.

BST validity checker overview
This lab requires implementation of a BST validity checker that identifies each type of problem mentioned above. The validity checker can be used to assist with BST implementations.

Determining how to identify key-related problems is part of this lab's requirements. As for identifying child-related problems, consider a preorder traversal of the two example trees above. A preorder traversal of either encounters the same node more than once. So the two child-related problems can be described with a single criterion: A distinct node is visited more than once during preorder traversal.

Ex: In the left tree, preorder traversal visits node 50, 25, 37, 75, 88, 75 again, and 88 again.
Ex: In the right tree, preorder traversal visits node 44, 22, 11, 33, 55, and then repeats in an infinite cycle.
So an algorithm to check the validity of BST should stop as soon as any node is visited more than once. Ex: The second visit of 75 stops traversal in the left tree and the second visit of 44 stops traversal in the right tree.


Step 1: Inspect the BSTNode.py file
Inspect the class declaration for a BST node in BSTNode.py. Each node has a key, a left child, and a right child. BSTNode.py is read-only, since no changes are required.


Step 2: Implement the BSTChecker.check_BST_validity() method
Implement the check_BST_validity() method in the BSTChecker class in the BSTChecker.py file. The method takes the tree's root node as an argument. If the tree is a valid BST, None must be returned. Otherwise the first-encountered problematic node must be returned.

Example figures above show the problematic node in red. Implement a preorder traversal that tracks necessary information, like the valid key range for a node's key and a set of visited nodes. As soon as a violation is encountered, like a node's key being out of range or a node being visited a second time, return that node.

Code in main.py creates a variety of trees and runs test cases. Ensure that all tests in main.py pass before submitting code for grading
