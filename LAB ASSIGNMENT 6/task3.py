import heapq
def dijkstra(graph, start, end):
  n = len(graph)
  dist = [float('inf')] * (n+1)
  dist[start] = 0
  pq = [(0, start)]
  while pq:
    d, u = heapq.heappop(pq)
    if u == end:
      return dist[u]
    if d > dist[u]:
      continue
    for v, w in graph[u]:
      new_dist = max(dist[u], w)
      if new_dist < dist[v]:
        dist[v] = new_dist
        heapq.heappush(pq, (new_dist, v))
  return "Impossible"
inp = open("D:\CSE221\LAB ASSIGNMENT 6\input3.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 6\output3.txt","w")
v, e = map(int, inp.readline().split())
graph = {}
for i in range(1, v+1):
    graph[i] = []
for i in range(e):
    f,l,w = list(map(int, inp.readline().split()))
    graph[f].append((l,w))
out.write(str(dijkstra(graph, 1, v))+"\n")
inp.close()
out.close()