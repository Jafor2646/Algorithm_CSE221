def dfs(lst, u, visited):
    visited[u] = 1
    out.write(str(u)+" ")
    for j in range(len(lst[u])):
        if visited[lst[u][j]] == 0:
            dfs(lst, lst[u][j], visited) 
inp = open("D:\CSE221\LAB ASSIGNMENT 4\input3.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output3.txt", "w")
v,e = list(map(int, inp.readline().split()))
adj_list = [[] for i in range(v+1)]
for i in range(e):
    f,l,= list(map(int, inp.readline().split()))
    adj_list[f].append(l)
    adj_list[l].append(f)
visited = [0]*(v+1)
for i in range(1,len(visited)):
    if visited[i] == 0:
        dfs(adj_list, i, visited)
inp.close()
out.close()