class Node:
    """ class to create a nodes for the tree"""

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.next = None


class BinaryTree:

    def __init__(self, value=None):
        self.root = None

    def pre_order(self, node=None, array_tree=None):
        """  root >> left >> right
        """

        if array_tree is None:
            array_tree = []

        node = node or self.root

        array_tree.append(node.value)

        if node.left:
            self.pre_order(node.left, array_tree)

        if node.right:
            self.pre_order(node.right, array_tree)

        return array_tree

    def in_order(self, node=None, array_tree=None):
        """ left >> root >> right
        """
        if array_tree is None:
            array_tree = []

        node = node or self.root

        if node.left:
            self.in_order(node.left, array_tree)

        array_tree.append(node.value)

        if node.right:
            self.in_order(node.right, array_tree)

        return array_tree

    def post_order(self, node=None, array_tree=[]):
        """  left >> right >> root
        """

        node = node or self.root

        if node.left:
            self.post_order(node.left, array_tree)

        if node.right:
            self.post_order(node.right, array_tree)

        array_tree.append(node.value)

        return array_tree

   


class BinarySearchTree(BinaryTree):
    """Class to create a Binary Search Tree """

    def add(self, value):
        """Method that accepts a value, and adds a new node with that value in the correct location 
        in the binary search tree"""

        node = Node(value)
        if self.root == None:
            self.root = node
            return

        current = self.root
        while True:
            if value < current.value:
                if current.left:
                    current = current.left
                else:
                    current.left = node
                    break
            else:  
                if current.right:
                    current = current.right
                else:
                    current.right = node
                    break

    def contains(self, value):
        """Method that accepts a value, and returns a boolean indicating whether or not the value is 
        in the tree at least once."""

        if self.root == None:
            raise myException("Tree is empty")

        current = self.root

        while current:

            if current.value == value:
                return True

            if current.value > value:
                current = current.left

            else:
                current = current.right
        return False

    def findMax(self):
        """ Finds the maximum value in a binary tree """
        return self.pre_order(self.root)[-1]  # will return the last element in the list of pre_order


if __name__ == '__main__':
    tree = BinarySearchTree()
    tree.add(89)
    tree.add(12)
    tree.add(14)
    tree.add(99)
    tree.add(-26)
    tree.add(103)
    tree.add(20)
    tree.add(18)
    tree.add(24)
    tree.add(56)
    tree.add(76)
    tree.add(3)
    print(tree.findMax())
    # [89, 12, -26, 3, 14, 20, 18, 24, 56, 76, 99, 103]
    print(tree.pre_order())
    print(tree.findMax())
