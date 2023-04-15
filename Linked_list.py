class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head == None:
            self.head = new_node

        else:
            current = self.head
            while current.next is not None:
                current = current.next

            current.next = new_node

    def print_llist(self):
        current = self.head
        
        while current is not None:
            if current.next is not None:
                print(current.data, "->", end="")
            else:
                print(current.data)
            current = current.next

linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)



# linked_list = LinkedList()
# linked_list.add_node(1)
# linked_list.add_node(2)
# linked_list.add_node(3)

# current_node = linked_list.head
# while current_node is not None:
#     print(current_node.__dict__)
#     current_node = current_node.next
# {'data': 1, 'next': <__main__.Node object at 0x7f6f0f7984c0>}
# {'data': 2, 'next': <__main__.Node object at 0x7f6f0f798580>}
# {'data': 3, 'next': None}
