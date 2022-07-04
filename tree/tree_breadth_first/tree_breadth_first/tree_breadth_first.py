class Node:
   

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def breadth_first(root=None):
    try:
        queue = [root]
        node_list = []
        while queue:
            current_node = queue.pop(0)
            node_list.append(current_node.value)
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

        return node_list

    except AttributeError:
        return "enter the root"


if __name__ == "__main__":
  pass