class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    flag = True
    minValue = 100000
    for i in range(len(self.storage)):
      if self.storage[i] == None:
        self.storage[i] = item
        flag = False
        break
    if self.storage[len(self.storage) - 1] != None:
      for i in range(len(self.storage)):
        if ord(self.storage[i]) < minValue:
          minValue = ord(self.storage[i])
    while flag:
      for i in range(len(self.storage)):
        if self.storage[i] == None:
          self.storage[i] = item
          flag = False
          break
        elif self.storage[len(self.storage) - 1] != None:
          if ord(self.storage[i]) == minValue:
            self.storage[i] = item
            flag = False
            break
          

  def get(self):
    storage = []
    for i in self.storage:
      if i != None:
        storage.append(i)
    return storage


# A ring buffer is a non-growable buffer with a fixed size. When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds elements to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

# For example:

# ```python
# buffer = RingBuffer(3)

# buffer.get()   # should return []

# buffer.append('a')
# buffer.append('b')
# buffer.append('c')

# buffer.get()   # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']



