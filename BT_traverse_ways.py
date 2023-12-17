# To perform a post-order traversal of a binary tree in Python, you can use either a recursive approach 
# or an iterative approach using a stack. 
# Here's how you can implement post-order traversal using both methods:

# METHOD - 1
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal_recursive(root):
    if root:
        post_order_traversal_recursive(root.left)
        post_order_traversal_recursive(root.right)
        print(root.value, end=" ")

# Example usage:
# Construct a sample binary tree:
#        1
#       / \
#      2   3
#     / \
#    4   5

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print("Post-order traversal (Recursive):")
post_order_traversal_recursive(root)

#METHOD - 2: Iterative Approach using a STACK:

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal_iterative(root):
    if not root:
        return
    
    result = []
    stack = []
    stack.append(root)

    while stack:
        current = stack.pop()
        result.insert(0, current.value)  # Insert at the beginning to reverse the order

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    for node_val in result:
        print(node_val, end=" ")

# Example usage (using the same binary tree as in the previous example):

print("\nPost-order traversal (Iterative):")
post_order_traversal_iterative(root)

#METHOD - 2: Iterative Approach using a QUEUE:

from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def post_order_traversal_queue(root):
    if not root:
        return
    
    result = []
    stack = [root]
    output = deque()

    while stack:
        current = stack.pop()
        output.appendleft(current)  # Insert at the beginning to reverse the order

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    while output:
        node = output.popleft()
        result.append(node.value)

    for node_val in result:
        print(node_val, end=" ")

# Example usage (using the same binary tree as in the previous examples):

print("Post-order traversal (Queue):")
post_order_traversal_queue(root)
