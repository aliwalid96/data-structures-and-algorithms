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