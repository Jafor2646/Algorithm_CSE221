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
inp = open("D:\CSE221\LAB ASSIGNMENT 7\input1.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 7\output1.txt","w")
n = int(inp.readline())
queue = PriorityQueue()
for i in range(n):
    ls = list(map(int, inp.readline().split()))
    queue.enqueue(ls)
interval = []
while not queue.isEmpty():
    f, s= queue.dequeue()
    if len(interval) == 0:
        interval.append((f,s))
    else:
        if f >= interval[len(interval)-1][1]:
            interval.append((f,s))
out.write(str(len(interval))+"\n")
for i in range(len(interval)):
    out.write(" ".join(str(j) for j in interval[i])+"\n")
inp.close()
out.close()