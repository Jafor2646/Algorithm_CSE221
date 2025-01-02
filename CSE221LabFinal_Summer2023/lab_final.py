#Set b
class PriorityQueue():
    def __init__(self):
        self.queue = []
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
    def isEmpty(self):
        return len(self.queue) == 0
    def insert(self, data):
        self.queue.append(data)
    def delete(self):
        min_val = 0
        for i in range(len(self.queue)):
            if self.queue[i][0] < self.queue[min_val][0]:
                min_val = i
        item = self.queue[min_val]
        del self.queue[min_val]
        return item[1]  
def countPath(graph, u, d, visited, pathCount):
    visited[u] = True
    if u == d:
       pathCount[0] += 1
    else:
       for i in range(len(graph[u])):
          if visited[graph[u][i][0]] == False:
             countPath(graph, graph[u][i][0], d, visited, pathCount)
    visited[u] = False
             
inp = open("D:\CSE221\LabsectionNo11_23341109_CSE221LabFinal_Summer2023\lab_final_input.txt","r")
out = open("D:\CSE221\LabsectionNo11_23341109_CSE221LabFinal_Summer2023\lab_final_output.txt","w")
n,m = list(map(int, inp.readline().split()))
graph = [[] for i in range(n)]
for i in range(m):
    u,v,w= list(map(int, inp.readline().split()))
    graph[u].append((v,w))
out.write("Output A:\n")
for i in range(len(graph)):
    out.write(str(i)+": ")
    if len(graph[i]) == 0:
       out.write("\n")
    else:
        for j in range(len(graph[i])):
          if j == len(graph[i])-1:
            out.write(str(graph[i][j][0])+"->"+str(graph[i][j][1])+"\n")
          else:
            out.write(str(graph[i][j][0])+"->"+str(graph[i][j][1])+" , ")        
out.write("Output B:\n")
visited = [False]*(n)
pathCount = [0]
countPath(graph, 0, 5, visited, pathCount)
out.write("Total "+str(pathCount[0])+" paths\n")
out.write("Output C:\n")
distance = [float("inf")]*(n)
distance[0] = 0
parent = [-1]*n
svisited = [False]*(n)
queue = PriorityQueue()
queue.insert((0,0))
while not queue.isEmpty():
   u = queue.delete()
   svisited[u] = True
   if u == 5:
      break
   for i in graph[u]:
      if svisited[i[0]] == False:
         if distance[i[0]] > (distance[u] + i[1]):
            distance[i[0]] = distance[u] + i[1]
            parent[i[0]] = u
            queue.insert((distance[i[0]], i[0]))
path = ""
i = 5
while i != -1:
    if i == 0:
      path = str(i)+path
    else:
      path = "->"+str(i)+path
    i = parent[i]
out.write(path+"\n")
out.write("Output D:\n")
out.write(str(distance[5])+" Unit Time")