from stack_and_queue.stack_and_queue import Node,Stack
import pytest

def test_push(stack):


  actual = stack.top.value
  expected = 2
  assert actual == expected
  
def test_pop(stack):
 

  actual= stack.pop()
  expected =2
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