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

    def length_(self):
        """length method will help to determine the length of 
        the list to use it in the kth_form_end() func """
        length = 0
        current = self.head
        while current:
            length += 1
            current = current.next
        return length

    def kth_from_end(self, k):
        """kth from end
        argument: a number, k, as a parameter.
        Return the nodes value that is k places from the tail of the linked list """

        length = self.length_()
        if not -length <= k < length:
            return ("k not in the range")
        next_node = None
        if k >= 0:
            next_node = length - k - 1
        if k < 0:
            next_node = k - 1
        current = self.head
        #"we don't care about the iterator value, just that it should run some specific number of times"
        for _ in range(next_node):
            """When you are not interested in some values returned by a function we use underscore in place 
            of variable name . Basically it means you are not interested in how many times the loop 
            is run till now just that it should run some specific number of times overall."""
            current = current.next
        return current.value



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

            

