class Queue:
  def __init__(self,length):
      self.frontpointer = -1
      self.rearpointer = 0
      self.length = length
      self.queue = []
      for i in range(length): (self.queue).append(None)
  def is_empty(self):
      return self.frontpointer == -1

  def is_full(self):
      return (self.rearpointer - self.frontpointer) == self.length + 1

  def dequeue(self):
      self.frontpointer = self.frontpointer + 1
      if not(self.is_empty()):
          (self.queue)[self.frontpointer] = None #Efficiency saves memory
          self.frontpointer = self.frontpointer + 1
      
  def enqueue(self,item):
      if not(self.is_full()):
          (self.queue)[self.rearpointer] = item
          self.rearpointer = self.rearpointer + 1
          

  def getqueue(self):
      return self.queue
          
queue1 = Queue(3)
queue1.dequeue()
queue1.enqueue("a")
print(queue1.getqueue())
queue1.enqueue("b")
print(queue1.getqueue())
queue1.enqueue("c")
print(queue1.getqueue())
queue1.dequeue()
print(queue1.getqueue())
