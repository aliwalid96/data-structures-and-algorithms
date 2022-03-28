from stack_and_queue.stack_and_queue import Stack,Node,Queue

import pytest
"""
for the stack :
    it push and pop and peek return the top value 
    and is empty return true when its empty and if its empty and tried to pop 
    print message (its empty)
for queue als do the same of the stack
"""

def test_push(stack):

  actual = stack.top.value
  expected = 2
  assert actual == expected
  
def test_pop(stack):
  actual= stack.pop()
  expected =2
  assert actual == expected

def test_pop_with_empty(stack):
  actual= stack.pop()
  actual= stack.pop()
  actual= stack.pop()
  actual= stack.pop()


  expected ="its empty"
  assert actual == expected


def test_peek_of_stack(stack):
  

  actual = stack.peek()
  expected = 2
  assert actual == expected


def test_is_empty_stack():
  stack=Stack()
  actual = stack.is_empty()
  expected = True
  assert actual == expected
  

 #decorator
@pytest.fixture
def stack():
 
  stack = Stack()
  stack.push(5)
  stack.push(3)
  stack.push(2)

  return stack


def test_enqueue(queue):
  actual = queue.rear.value
  expected = "raghad"
  assert actual == expected
  

  
def test_dequeue(queue):
  actual = queue.dequeue()
  expected = None
  assert actual == expected

def test_peek(queue):
  actual = queue.peek()
  expected = "zaid"
  assert actual == expected


def test_is_empty(queue):
  actual = queue.is_empty()
  expected = None
  assert actual == expected


  
@pytest.fixture
def queue():
  queue=Queue()
  queue.enqueue("zaid")
  queue.enqueue("raneem")
  queue.enqueue("raghad")
  return queue