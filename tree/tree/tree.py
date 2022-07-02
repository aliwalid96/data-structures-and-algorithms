
class newNode:
 
    # Construct to create a new node
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
 
# A utility function to do inorder
# traversal of BST
def inorder( root) :
 
    if (root != None):
        inorder(root.left)
        print(root.key, end = " ")
        inorder(root.right)
     
""" A utility function to insert a
new node with given key in BST """
def insert(node, key):
 
    """ If the tree is empty,
    return a new node """
    if (node == None):
        return newNode(key)
 
    """ Otherwise, recur down the tree """
    if (key < node.key):
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
 
    """ return the (unchanged) node pointer """
    return node
 
# Function to print all even nodes
def oddNode(root) :
 
    if (root != None):
        oddNode(root.left)
         
        # if node is even then print it
        if (root.key % 2 != 0):
            print(root.key, end = " ")
        oddNode(root.right)
 
# Driver Code
if __name__ == '__main__':
     
    """ Let us create following BST
    5
    / \
    3 7
    / \ / \
    2 4 6 8 """
    root = None
    root = insert(root, 5)
    root = insert(root, 3)
    root = insert(root, 2)
    root = insert(root, 4)
    root = insert(root, 7)
    root = insert(root, 6)
    root = insert(root, 8)
 
    oddNode(root)
 
# This code is contributed by
# Shubham Singh(SHUBHAMSINGH10)