class Node():

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class LinkedList():

    def __init__(self):
        self.head = None

    def ToString(self):
        """return the str method """
        return self.__str__()

    def __str__(self):
        values = '  Head-->  '
        if self.head is None:
            values = 'This Linked List is empty'
        else:
            current = self.head
            while (current):
                values += f'{current.value}->  '
                current = current.next
            values += "None"
        return values

    def insert(self, new_node):
        """ add a node to the linked list"""
        if new_node == '':
            raise TypeError('Node must not be empty')
        else:
            new_node.next = self.head
            self.head = new_node

    def includes(self, value):
        if value is None:
            raise TypeError('missing value argument')
        else:
            current = self.head
            while current:
                if current.value == value:
                    return True
                current = current.next
            # print(value)
            return False


if __name__ == '__main__':
    # ll = LinkedList()
    # a = Node("a")
    # b = Node("b")
    # c = Node("c")
    # ll.insert(a)
    # ll.insert(b)
    # ll.insert(c)
    # print(ll.head.value)
    # list_insert = LinkedList()
    # list_insert.insert(Node(1))
    # list_insert.insert(Node(2))
    # list_insert.insert(Node(3))

    # print(list_insert.ToString())

    # ll = LinkedList()
    # a = Node("a")
    # b = Node("b")
    # ll.insert(b)
    # ll.insert(a)
    # print(ll.includes('abc'))
    # print(ll.includes('a'))
    list_str = LinkedList()
    list_str.insert(Node(1))
    list_str.insert(Node(2))
    list_str.insert(Node(3))
    list_str.insert(Node(4))
    list_str.insert(Node(5))
    print(list_str.__str__())
    expected = '  Head-->  1->  2->  3->  4->  5->  None'
    print(expected)
    
    pass

            

