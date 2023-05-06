class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = Node(root_value)

    def add_node(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
        else:
            self._add_node_recursive(new_node, self.root)

    def _add_node_recursive(self, new_node, current_node):
        if new_node.value < current_node.value:
            if current_node.left_child is None:
                current_node.left_child = new_node
            else:
                self._add_node_recursive(new_node, current_node.left_child)
        elif new_node.value > current_node.value:
            if current_node.right_child is None:
                current_node.right_child = new_node
            else:
                self._add_node_recursive(new_node, current_node.right_child)

    def search(self, value):
        return self._search_recursive(value, self.root)

    def _search_recursive(self, value, current_node):
        if current_node is None or current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._search_recursive(value, current_node.left_child)
        else:
            return self._search_recursive(value, current_node.right_child)



tree = BinaryTree(5)
tree.add_node(3)
tree.add_node(7)
tree.add_node(2)
tree.add_node(4)
tree.add_node(6)
tree.add_node(8)

print(tree.search(4).value) # Output: 4
print(tree.search(9)) # Output: None
