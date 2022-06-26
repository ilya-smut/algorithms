class Node:
    def __init__(self, parent, first_child, next_sibling, key):
        self.parent = parent
        self.first_child = first_child
        self.next_sibling = next_sibling
        self.key = key

    def is_head(self):
        return self.parent is None

    def print_key(self):
        print(self.key)

    def has_next_sibling(self):
        return self.next_sibling is not None

    def has_a_child(self):
        return self.first_child is not None

def preorder_traversal_recursive(starting_node):
    starting_node.print_key()
    if starting_node.has_a_child():
        preorder_traversal_recursive(starting_node.first_child)
    if starting_node.has_next_sibling():
        preorder_traversal_recursive(starting_node.next_sibling)


def preorder_traversal(starting_node):
    current_node = starting_node
    current_node.print_key()
    flag = True
    while True:
        if current_node.has_a_child() and flag:
            current_node = current_node.first_child
            current_node.print_key()
        elif current_node.has_next_sibling():
            current_node = current_node.next_sibling
            flag = True
            current_node.print_key()
        elif current_node.parent is not None:
            current_node = current_node.parent
            flag = False
        elif current_node.parent is None:
            break


def postorder_traversal_recursive(starting_node):
    if starting_node.has_a_child():
        postorder_traversal_recursive(starting_node.first_child)
    if starting_node.has_next_sibling():
        starting_node.print_key()
        postorder_traversal_recursive(starting_node.next_sibling)
    else:
        starting_node.print_key()







head = Node(None, Node, None, '0')

node_1_1 = Node(head, Node, Node, '1_1')
head.first_child = node_1_1
node_1_2 = Node(head, Node, Node, '1_2')
node_1_1.next_sibling = node_1_2
node_1_3 = Node(head, Node, None, '1_3')
node_1_2.next_sibling = node_1_3

node_2_1 = Node(node_1_1, None, Node, '2_1')
node_1_1.first_child = node_2_1
node_2_2 = Node(node_1_1, None, None, '2_2')
node_2_1.next_sibling = node_2_2

node_2_3 = Node(node_1_2, None, Node, '2_3')
node_1_2.first_child = node_2_3
node_2_4 = Node(node_1_2, None, None, '2_4')
node_2_3.next_sibling = node_2_4

node_2_5 = Node(node_1_3, None, None, '2_5')
node_1_3.first_child = node_2_5

preorder_traversal_recursive(head)
print()
preorder_traversal(head)
print()
postorder_traversal_recursive(head)
print()

