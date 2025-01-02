from queue import Queue
inp = open("D:\CSE221\LAB ASSIGNMENT 4\input5.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output5.txt","w")
v,e, d = list(map(int, inp.readline().split()))
adj_list = [[] for i in range(v+1)]
for i in range(e):
    f,l,= list(map(int, inp.readline().split()))
    adj_list[f].append(l)
    adj_list[l].append(f)
visited = [-1]*(v+1)
path = [0]*(v+1)
q = Queue(maxsize=v)
for i in range(len(adj_list)):
    if len(adj_list[i]) != 0:
        q.put(i)
        visited[i] = 0
        break
while q.empty() != True:
    u = q.get()
    for j in range(len(adj_list[u])):
        if visited[adj_list[u][j]] == -1:
          visited[adj_list[u][j]] = visited[u]+1
          path[adj_list[u][j]] = u
          q.put(adj_list[u][j])
out.write("Time: "+ str(visited[d])+"\n")
s = ""
i = d
while i != 0:
    s = str(i)+" "+s
    i = path[i]
out.write("Shortest Path: "+s)
inp.close()
out.close()