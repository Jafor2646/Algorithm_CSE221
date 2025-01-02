class PriorityQueue:
    def __init__(self):
        self.lst = []
    def isEmpty(self):
        return len(self.lst) == 0
    def enqueue(self, e):
        self.lst.append(e)
    def dequeue(self):
        mini = self.lst[0]
        minIdx = 0
        for i in range(1, len(self.lst)):
            if self.lst[i][1] <= mini[1]:
                if self.lst[i][1] == mini[1]:
                    if self.lst[i][0] < mini[0]:
                        mini = self.lst[i]
                        minIdx = i
                else:
                    mini = self.lst[i]
                    minIdx = i
        temp = self.lst[minIdx]
        del self.lst[minIdx]
        return temp
inp = open("D:\CSE221\LAB ASSIGNMENT 7\input2.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 7\output2.txt","w") 
n,m = list(map(int,inp.readline().split()))
emp = [0]*m
queue = PriorityQueue()
for i in range(n):
    ls = list(map(int, inp.readline().split()))
    queue.enqueue(ls)
count = 0
while not queue.isEmpty():
    f, s= queue.dequeue()
    idx = 0
    flag = False
    for i in range(len(emp)):
      if emp[i] == f:
          emp[i] = s
          count += 1
          flag = False
          break
      if emp[i] == 0:
          emp[i] = s
          count += 1
          flag = False
          break
      if emp[i] <= f:
          flag = True
          if emp[i] > emp[idx]:
              idx = i
    if flag:
        emp[idx] = s
        count += 1
out.write(str(count))
inp.close()
out.close()