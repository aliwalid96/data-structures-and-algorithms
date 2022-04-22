from linked_list.linked_list import LinkedList,Node


def test_list_creation():
    actual =LinkedList()
    assert actual.head == None


def test_empty_linked_list():
    ll = LinkedList()
    assert ll.head == None


def test_multiple_nodes():
    ll = LinkedList()
    a = Node("a")
    b = Node("b")
    c = Node("c")
    ll.insert(a)
    ll.insert(b)
    ll.insert(c)
    assert ll.head.value == 'c'
    assert ll.head.next.value == 'b'
    assert ll.head.next.next.value == 'a'


def test_insert_method():
    list_insert = LinkedList()
    list_insert.insert(Node(1))
    list_insert.insert(Node(2))
    list_insert.insert(Node(3))

    expected = '  Head-->  3->  2->  1->  None'
    actual = list_insert.ToString()
    assert expected == actual


def test_includes_if_false():
    ll = LinkedList()
    a = Node("a")
    b = Node("b")
    ll.insert(b)
    ll.insert(a)
    assert ll.includes('abc') == False


 # “Happy Path” where k is not at the end, but somewhere in the middle of the linked list   
def test_kth_greater_than_the_list():
    ll = LinkedList()
    ll.insert(Node(10))
    ll.insert(Node(20))
    ll.insert(Node(30))
    ll.insert(Node(40))
    expected = "k not in the range"
    actual = ll.kth_from_end(6)
    assert expected == actual


def test_the_linked_list_size_is_one():
    ll = LinkedList()
    ll.insert(Node(10))
    expected = 10
    actual = ll.kth_from_end(0)
    assert expected == actual


def test_kth_is_negative_int():
    ll = LinkedList()
    ll.insert(Node(10))
    ll.insert(Node(20))
    ll.insert(Node(30))
    ll.insert(Node(40))
    expected = "k not in the range"
    actual = ll.kth_from_end(-2)
    assert expected


def test_kth_and_ll_are_the_same():
    ll = LinkedList()
    ll.insert(Node(10))
    ll.insert(Node(20))
    ll.insert(Node(30))
    ll.insert(Node(40))
    expected = 40
    actual = ll.kth_from_end(0)
    assert expected == actual


def test_happy_path():
    ll = LinkedList()
    ll.insert(Node('1'))
    ll.insert(Node('2'))
    ll.insert(Node('3'))
    ll.insert(Node('4'))
    assert ll.kth_from_end(2) == '3'
