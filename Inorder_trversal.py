class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.data = key

# self implementation.
def inorder_traversal(root):
    # wrong: already in root -> left. 
    # if root.left:
    if root:
        inorder_traversal(root.left)
        print(root.data)

    # if root.right:
        inorder_traversal(root.right)
    return None

# Driver code 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

# best implementation.
# A function to do inorder tree traversal 
def printInorder(root): 
  
    if root: 
  
        # First recur on left child 
        printInorder(root.left) 
  
        # then print the data of node 
        print(root.val), 
  
        # now recur on right child 
        printInorder(root.right) 

  
# op : 4 2 5 1 3