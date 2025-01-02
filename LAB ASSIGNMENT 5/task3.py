def stronglyConnectedComponents(graph, v, visited, temp):
    visited[v] = True
    temp.append(v)
    for i in graph[v]:
        if visited[i] == False:
            stronglyConnectedComponents(graph, i, visited, temp)
def dfs(graph, u, visited, stack):
    visited[u] = True
    for i in graph[u]:
        if visited[i] == False:
            dfs(graph, i, visited, stack)
    stack.append(u)
inp = open("D:\CSE221\LAB ASSIGNMENT 5\input3.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 5\output3.txt","w")  
v, e = list(map(int, inp.readline().split()))
graph = {}
revGraph = {}
for i in range(1, v+1):
    graph[i] = []
    revGraph[i] = []
for i in range(e):
    f, l = list(map(int, inp.readline().split()))
    graph[f].append(l)
    revGraph[l].append(f)
stack = []
scc = []
visited = [False]*(v+1)
revVisited = [False]*(v+1)
for i in range(1, v+1):
    if revVisited[i] == False:
        dfs(revGraph, i, revVisited, stack)
while stack:
    e = stack.pop()
    if visited[e] == False:
        temp = []
        stronglyConnectedComponents(graph, e, visited, temp)
        scc.append(temp)
for i in range(len(scc)-1, -1, -1):
    out.write(" ".join(str(scc[i][j]) for j in range(len(scc[i])))+"\n")
inp.close()
out.close()
