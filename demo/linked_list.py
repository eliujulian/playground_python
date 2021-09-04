"""
My own implementation of Linked List Structure.
"""


class Node:
    def __init__(self, value, pointer):
        self.value = value
        self.pointer = pointer
        self.previous = None

    def __str__(self):
        result = f"{self.name()}-Node (value: {str(self.value)}"
        if self.pointer:
            result += f", points_to: {str(self.pointer.value)}"
        if self.previous:
            result += f", ref from: {str(self.previous.value)}"
        result += ")"
        return result

    def is_start(self):
        return not self.pointer

    def is_end(self):
        return not self.previous

    def name(self):
        if self.is_start():
            return "Start"
        elif self.is_end():
            return "End"
        else:
            return "Chain"


def create_linked_list(n):
    node = Node(0, None)
    for n in range(1, n):
        new_node = Node(n, node)
        node.previous = new_node
        node = new_node
    return node


def go_to_start(node):
    if not node.pointer:
        return node
    while node:
        if not node.pointer.pointer:
            return node.pointer
        else:
            node = node.pointer


def got_to_end(node):
    if not node.previous:
        return node
    while node:
        if not node.previous.previous:
            return node.previous
        else:
            node = node.previous


def reverse_list(node):
    node = go_to_start(node)
    while True:
        previous = node.previous
        node.pointer, node.previous = node.previous, node.pointer
        if previous:
            node = previous
        else:
            break
    return node


def find_element(search_value: int, node):
    if not node.is_start():
        return None, 0
    counter = 0
    while True:
        counter += 1
        if node.value == search_value:
            return node, counter
        elif node.previous:
            node = node.previous
        else:
            break
    return None, counter


def report(node):
    print("")
    print("Linked List: ")
    if node.is_end():
        while True:
            print(node)
            if node.pointer:
                node = node.pointer
            else:
                break
    elif node.is_start():
        while True:
            print(node)
            if node.previous:
                node = node.previous
            else:
                break
    else:
        report(go_to_start(node))


def main():
    node = create_linked_list(10)
    report(node)

    node = go_to_start(node)
    print("Start ", node)
    node = got_to_end(node)
    print("End ", node)

    print("Reversing list: ")
    reverse_list(node)

    report(node)

    reverse_list(node)

    print("Searching for node 5")
    node, count = find_element(5, go_to_start(node))
    print("Element: ", node, " Steps: ", count)


if __name__ == '__main__':
    main()
