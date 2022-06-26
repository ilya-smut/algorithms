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


def check_existence_of_the_layer(working_node, number_of_steps):
    node_in_process = working_node
    if number_of_steps == 0:
        return True
    for i in range(number_of_steps):
        if node_in_process.has_a_child():
            node_in_process = node_in_process.first_child
        else:
            return False
    return node_in_process.has_a_child()


def preorder_traversal(head_of_the_tree):
    number_of_steps = 0

    if not head_of_the_tree.is_head():
        return None

    def go_one_layer(working_node):
        while True:
            working_node.print_key()
            if working_node.has_next_sibling():
                working_node = working_node.next_sibling
            elif working_node.parent.has_next_sibling():
                if working_node.parent.next_sibling.has_a_child():
                    working_node = working_node.parent.next_sibling.first_child
            elif not working_node.parent.has_next_sibling():
                    break
        return working_node

    head_of_the_tree.print_key()
    current_node = head_of_the_tree.first_child

    while check_existence_of_the_layer(head_of_the_tree, number_of_steps):
        go_one_layer(current_node)
        number_of_steps += 1
        current_node = current_node.first_child






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

preorder_traversal(head)

