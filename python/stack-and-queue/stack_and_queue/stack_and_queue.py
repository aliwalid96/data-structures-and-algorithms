class Node :
  """
  this class to creat a node that point to null
  """
  def __init__(self,value):
    self.value=value
    self.next=None 

class Stack :
  """creat a stack and the top point to null"""
  def __init__(self,node=None):
    self.top = node 

  def push(self,value):
    """this method to add a node to stack"""
    node = Node(value)
    node.next = self.top
    self.top = node 

  def pop(self) :
    """ this method to delete a node from stack"""
    try:
      if self.top != None:
        temp = self.top
        self.top = self.top.next
        temp.next= None
      else:
        return "its empty"

      return temp.value
    except:  
      raise Exception("its empty")

  def peek(self):
    """this method to return the top value """

    return self.top.value
   
  def is_empty(self):
    """method to check if stack is impty
     return true
    """
    return self.top == None 
     # return self.top


class Queue :
  """
    This class creates queue that Front and Back point to null
    """
  def __init__(self):
    self.front=None
    self.rear=None

  def enqueue(self,value):
    """this method to add a node to queue """
    node = Node(value)

    if not self.front :
      self.rear = node 
      self.front = node 
      
    else:  
      self.rear.next = node 
      self.rear = node 
      
  def dequeue(self):
        """this method to delete a node from queu"""
        if self.rear == self.front:
            self.rear = None
            self.front = self.front.next
        elif self.rear == None:
            Exception("its empty")
        return

  def is_empty(self):
    """this method return true if the front is null """
    try:
      if self.rear == None:
        return 
    except:
      Exception("the queue is empty")
   

  def peek(self):
    """this method return true if the front .value is null"""
    return self.front.value

