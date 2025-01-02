def dfs(graph, u, visited, stack):
    visited[u] = True
    for i in range(len(graph[u])):
        if visited[graph[u][i]] == False:
            dfs(graph, graph[u][i], visited, stack)
    stack.append(u)
def detectCycle(graph, stack):
    pos = dict()
    idx = 0
    while(len(stack) != 0):
        pos[stack[-1]] = idx
        idx += 1
        topOrder.append(stack[-1])
        stack.pop()
    for i in graph.keys():
        for j in graph[i]:
            f = pos[i]
            s = pos[j]
            if f>s:
                return True
    return False
inp = open("D:\CSE221\LAB ASSIGNMENT 5\input1a.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 5\output1a.txt","w")
v,e = list(map(int, inp.readline().split()))
graph = {}
for i in range(1,v+1):
    graph[i] = []
for i in range(e):
    f, l = list(map(int, inp.readline().split()))
    graph[f].append(l)
visited = [False]*(v+1)
stack = []
for i in range(1,len(visited)):
    if visited[i] == False:
        dfs(graph, i, visited, stack)
topOrder = []
if detectCycle(graph, stack):
    print("IMPOSSIBLE")
else:
    out.write(" ".join(str(topOrder[i]) for i in range(len(topOrder)))+"\n")
inp.close()
out.close()