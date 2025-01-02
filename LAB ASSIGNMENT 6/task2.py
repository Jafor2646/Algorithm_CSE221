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
def dijkstra(graph, s, distance, parent, visited):
    queue = PriorityQueue()
    queue.insert((0,s))
    distance[s] = 0
    visited[s] = True
    while not queue.isEmpty():
        u = queue.delete()
        visited[u] = True
        for i in graph[u]:
            if visited[i[0]] == False:
                if distance[i[0]] > (distance[u]+i[1]):
                    distance[i[0]] = distance[u]+i[1]
                    parent[i[0]] = u
                    queue.insert((distance[i[0]], i[0]))
inp = open("D:\CSE221\LAB ASSIGNMENT 6\input2.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 6\output2.txt","w")
v, e = list(map(int, inp.readline().split()))
graph = {}
for i in range(1, v+1):
    graph[i] = []
for i in range(e):
    f,l,w = list(map(int, inp.readline().split()))
    graph[f].append((l,w))
distanceA = [float("inf")]*(v+1)
parentA = [0]*(v+1)
distanceB = [float("inf")]*(v+1)
parentB = [0]*(v+1)
visitedA = [False]*(v+1)
visitedB = [False]*(v+1)
s1, s2 = list(map(int,(inp.readline().split())))
dijkstra(graph, s1,distanceA,parentA, visitedA)
dijkstra(graph, s2,distanceB,parentB, visitedB)
flag = True
common = []
for i in range(1, len(visitedA)):
    if visitedA[i] == True and visitedB[i] == True:
        if distanceA[i] > distanceB[i]:
            common.append((distanceA[i],i))
        else:
            common.append((distanceB[i],i))
        flag = False
        
if flag:
    print("Impossible")
else:
    t,n = min(common,key= lambda x: x[0])
    out.write(f"Time {t}\nNode {n}")
inp.close()
out.close()