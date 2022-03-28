
def Reversed(list):
  prev = None 
  current = list.head

  while current != None:
    next = current.next
    current.next = prev
    prev = current
    current = next

  return list

def is_palindrom(ll):
  ll2=Reversed(ll)
  current=ll.head
  current2=ll2.head
  middle=ll.size/2
  if ll.size %2==0:
    new_middle=middle.next
  else:
    new_middle=middle

  while current !=new_middle:
    if current !=current2:
      return False
    else:
      current=current.next
      current2=current2.next
  return True


