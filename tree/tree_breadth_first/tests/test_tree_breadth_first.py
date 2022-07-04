

from tree.tree_breadth_first.tree_breadth_first import Node, breadth_first


#Traversal expected [2, 3, 4, 5, 6] .
def test_Breadth_first():

    root = Node(2)
    root.left = Node(3)
    root.right = Node(4)
    root.left.left = Node(5)
    root.left.right = Node(6)

    assert breadth_first(root) == [2, 3, 4, 5, 6]


def test_Breadth_first_Error_Handling():
    assert breadth_first() == "enter the root"

