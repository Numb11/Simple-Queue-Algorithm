class Queue:
  def __init__(self,length):
      self.frontpointer = 0
      self.rearpointer = 0
      self.length = length
      self.queue = []
      for i in range(length): (self.queue).append(None)
  def size(self):
      count = 0
      for i in range(0,self.length):
          if self.queue[i] != None:
              count += 1
      return count
      
  def dequeue(self):
      if not(self.size() == 0):
          self.queue[self.frontpointer] = None
          if not(self.frontpointer == self.length-1):
           self.frontpointer = self.frontpointer +1 
          else:
           self.frontpointer = 0 


  def enqueue(self,item):
    if not(self.length == self.size()):
        self.queue[self.rearpointer] = item
        if not(self.rearpointer == self.length-1):
          self.rearpointer = self.rearpointer +1
        else:
          self.rearpointer = 0

  def getqueue(self):
        return self.queue
#A cheeky CLI
queue1 = Queue(int(input("Enter Queue length:")))
while True:
 print("-------------------------------")
 print("1.Dequeue an item")
 print("2.Enqueue an item")
 item = input("")
 if item == "1":
     queue1.dequeue()
     print(queue1.getqueue())
 elif item =="2":
     queue1.enqueue(input("Enter item:"))
     print(queue1.getqueue())
