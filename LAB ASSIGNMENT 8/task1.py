def find(parent, i):
    if parent[i] != i:
        parent[i] = find(parent, parent[i])
    return parent[i]
def union(parent, rank, x, y):
    a = find(parent,x)
    b = find(parent,y)
    if a == b:
        return
    if rank[a] > rank[b]:
        parent[b] = a
    else:
        parent[a] = b
        if rank[a] == rank[b]:
            rank[b] = rank[a]+1
inp = open("D:\CSE221\LAB ASSIGNMENT 8\input1.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 8\output1.txt","w")
v,e= list(map(int, inp.readline().split()))
graph = []
for i in range(e):
    lst = list(map(int, inp.readline().split()))
    graph.append(lst)
parent = [i for i in range(v+1)]
rank = [0]*(v+1)
graph = sorted(graph, key=lambda item: item[2])
cost = 0
i = 0
while i<e:
    u,v,w=graph[i]
    i += 1
    x = find(parent,u)
    y = find(parent,v)
    if x != y:
        cost += w
        union(parent, rank, x, y)
out.write(str(cost)+"\n")
inp.close()
out.close()