# Stacks and Queues
two kind of data structrue by adding node to them 
stack is first in last out 
queue first in first out 

## Challenge
try to add node and delete it and check if they are empty or not and in the stack the peek return the top value and in the queue peek return the front value 
## Approach & Efficiency


## API

## stack

### Push 
when we want to push an item 
the new node.next in the first =null
then we assighn the new node.next =top
then top = new node value 
### Pop is removing a node 
we declere new value temp=top
let it point to the top 

then top=top.next
change the top value to the next 
temp.next =null
then delet it by put the temp.next =null
### Peek 
return top.value 
### IsEmpty 
return true if top.value is null
## Queue

### Enqueue function to add a node 
to add node wa change the rear.next in the que to the new node 
rear =the new node
### Dequeue function in queue
firstly chek if its not empty by isempty function

he first thing you want to do is create a temporary reference type named temp and have it point to the same Node that front is pointing too.
then assign front to front.next 
then temp.next =null

### Peek 
return the front but firstly make sure its not empty by isempty function 
### IsEmpty 
return true if front is null

