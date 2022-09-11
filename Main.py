class Node:
  def __init__(self, data):
    self.data = data
    self.next = None


class Stack:
  def __init__(self):
    self.head = None

  def push(self, data) -> None:
    if self.head==None:
      self.head=Node(data)
    else:
      newnode=Node(data)
      newnode.next=self.head
      self.head=newnode
    

  def pop(self) -> None:
    poppednode = self.head
    self.head = self.head.next
    poppednode.next = None
    return poppednode.data

  def status(self):
    """
    It prints all the elements of stack.
    """
    iternode=self.head
    while(iternode != None):
 
          print(iternode.data, "->", end=" ")
          iternode = iternode.next
    return


# Do not change the following code
stack = Stack()
operations = []
for specific_operation in input().split(','):
    operations.append(specific_operation.strip())
input_data = input()
data = input_data.split(',')
for i in range(len(operations)):
  if operations[i] == "push":
    stack.push(int(data[i]))
  elif operations[i] == "pop":
    stack.pop()
stack.status()
