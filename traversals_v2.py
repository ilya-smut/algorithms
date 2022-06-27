from algorithms.traversals import postorder_traversal_recursive


class Node:
    def __init__(self, key):
        self.first_child = None
        self.next_sibling = None
        self.parent = None
        self.key = key

    def is_head(self):
        return self.parent is None

    def print_key(self):
        print(self.key, end=' ')

    def has_next_sibling(self):
        return self.next_sibling is not None

    def has_a_child(self):
        return self.first_child is not None


def postorder_recursive(starting_node):
    if starting_node.has_a_child():
        postorder_traversal_recursive(starting_node.first_child)
    if starting_node.has_next_sibling():
        starting_node.print_key()
        postorder_traversal_recursive(starting_node.next_sibling)
    else:
        starting_node.print_key()


def postorder_iterative(starting_node):
    gone_values = set()
    while True:
        if starting_node.has_a_child() and starting_node.first_child not in gone_values:
            starting_node = starting_node.first_child
        elif starting_node.has_next_sibling():
            gone_values.add(starting_node)
            starting_node.print_key()
            starting_node = starting_node.next_sibling
        elif not starting_node.has_next_sibling():
            if starting_node.parent is None:
                starting_node.print_key()
                break
            starting_node.print_key()
            starting_node = starting_node.parent



def preorder_recursive(starting_node):
    starting_node.print_key()
    if starting_node.has_a_child():
        preorder_recursive(starting_node.first_child)
    if starting_node.has_next_sibling():
        preorder_recursive(starting_node.next_sibling)


def preorder_iterative(starting_node):
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


gone_values_level_rec = set()
queue = []
def levelorder_recursive(node):
    global queue
    if node:
        print(node.key, end=' ')
        queue.append(node.first_child)
        levelorder_recursive(node.next_sibling)
        levelorder_recursive(queue.pop(0))


def levelorder_iterative(starting_node):
    iterated_list = []
    iterated_list.append(starting_node)
    for element in iterated_list:
        if element.has_a_child():
            iterated_list.append(element.first_child)
            if element.first_child.has_next_sibling():
                iterated_list.append(element.first_child.next_sibling)
    for element in iterated_list:
        element.print_key()


root = Node(1)
root.first_child = Node(2)
root.first_child.parent = root
root.first_child.next_sibling = Node(3)
root.first_child.next_sibling.parent = root
root.first_child.first_child = Node(4)
root.first_child.first_child.parent = root.first_child
root.first_child.first_child.next_sibling = Node(5)
root.first_child.first_child.next_sibling.parent = root.first_child
root.first_child.next_sibling.first_child = Node(6)
root.first_child.next_sibling.first_child.parent = root.first_child.next_sibling
root.first_child.next_sibling.first_child.next_sibling = Node(7)
root.first_child.next_sibling.first_child.next_sibling.parent = root.first_child.next_sibling


print("Preorder:")
print("\tRecursice -> ", end='')
preorder_recursive(root)
print("\n\tIterative -> ", end='')
preorder_iterative(root)
print()

print("Postorder:")
print("\tRecursice -> ", end='')
postorder_recursive(root)
print("\n\tIterative -> ", end='')
postorder_iterative(root)
print()

print("Levelorder:")
print("\tRecursice -> ", end='')
levelorder_recursive(root)
print("\n\tIterative -> ", end='')
levelorder_iterative(root)
print()


