from queue import Queue
inp = open("D:\CSE221\LAB ASSIGNMENT 4\input2.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output2.txt","w")
v,e = list(map(int, inp.readline().split()))
adj_list = [[] for i in range(v+1)]
for i in range(e):
    f,l,= list(map(int, inp.readline().split()))
    adj_list[f].append(l)
    adj_list[l].append(f)
visited = [0]*(v+1)
q = Queue(maxsize=v)
q.put(1)
visited[1] = 1
while q.empty() != True:
    u = q.get()
    out.write(str(u)+" ")
    for j in range(len(adj_list[u])):
        if visited[adj_list[u][j]] == 0:
          visited[adj_list[u][j]] = 1
          q.put(adj_list[u][j])
inp.close()
out.close()