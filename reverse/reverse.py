class Node:
  def __init__(self, value=None, next_node=None):
    # the value at this linked list node
    self.value = value
    # reference to the next node in the list
    self.next_node = next_node

  def get_value(self):
    return self.value

  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    # set this node's next_node reference to the passed in node
    self.next_node = new_next

class LinkedList:
  def __init__(self):
    # reference to the head of the list
    self.head = None

  def add_to_head(self, value):
    node = Node(value)
    if self.head is not None:
      node.set_next(self.head)
    
    self.head = node

  def contains(self, value):
    if not self.head:
      return False
    # get a reference to the node we're currently at; update this as we traverse the list
    current = self.head
    # check to see if we're at a valid node 
    while current:
      # return True if the current value we're looking at matches our target value
      if current.get_value() == value:
        return True
      # update our current node to the current node's next node
      current = current.get_next()
    # if we've gotten here, then the target node isn't in our list
    return False

  # thought process:  start at head and add to head the value, keep moving down the line and adding to head.  
  # setting the value of the head to the previous value at the head....
  # while true that self.next != None: add to head: when it does == None add it to the head and break....
  def reverse_list(self):
    flag = True
    if self.head:
      node = self.head
    if self.head:
      while flag:
        if not node.next_node:
          self.add_to_head(node.value)
          flag = False
          break
        else:
          self.add_to_head(node.value)
          node = node.get_next()


#   Inside of the `reverse` directory, you'll find a basic implementation of a Singly Linked List. _Without_ making it a Doubly Linked List (adding a tail attribute), complete the `reverse_list()` function within `reverse/reverse.py` reverse the contents of the list. 

# For example,
# ```
# 1->2->3->None
# ```
# would become...
# ```
# 3->2->1->None
# ```