def find(parent, n):
    if parent[n] != n:
        parent[n] = find(parent, parent[n])
    return parent[n]
        

def union(parent, rank, x, y):
    u = find(parent, x)
    v = find(parent, y)
    if u == v:     
        return rank[u]
    if rank[u] < rank[v]:
        parent[u] = v
        rank[v] += rank[u]
        return rank[v]
    elif rank[u] > rank[v]:
        parent[v] = u
        rank[u] += rank[v]
    else:
        parent[v] = parent[u]
        rank[u] += rank[v]
    return rank[u]
inp = open("D:\CSE221\LAB ASSIGNMENT 7\input3.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 7\output3.txt","w")    
n, q = list(map(int, inp.readline().split()))
rank = [1]*(n+1)
parent = [i for i in range(n+1)]
for i in range(q):
    a,b= list(map(int,inp.readline().split()))
    ans = union(parent, rank, a, b)
    out.write(str(ans)+"\n")
inp.close()
out.close()