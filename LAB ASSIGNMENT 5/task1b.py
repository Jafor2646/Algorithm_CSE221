inp = open("D:\CSE221\LAB ASSIGNMENT 5\input1b.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 5\output1b.txt","w")
v,e = list(map(int, inp.readline().split()))
graph = {}
for i in range(1,v+1):
    graph[i] = []
for i in range(e):
    f, l = list(map(int, inp.readline().split()))
    graph[f].append(l)
in_degree = [0]*(v+1)
queue = []
topOrder = []
for i in range(1,v+1):
    for j in graph[i]:
        in_degree[j] = in_degree[j] + 1
for i in range(1, len(in_degree)):
    if in_degree[i] == 0:
        queue.append(i)
count = 0
while queue:
    u = queue.pop(0)
    topOrder.append(u)
    for i in graph[u]:
        in_degree[i] -= 1
        if in_degree[i] == 0:
            queue.append(i)
    count += 1
if count == v:
    out.write(" ".join(str(topOrder[i]) for i in range(len(topOrder)))+"\n")                  
else:
    out.write("IMPOSSIBLE\n")
inp.close()
out.close()