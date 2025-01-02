def has_cycle(graph):
    def dfs(node):
        if visited[node]:
            return False

        visited[node] = True
        recursion_stack[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    return True
            elif recursion_stack[neighbor]:
                return True

        recursion_stack[node] = False
        return False

    num_nodes = len(graph)+1
    visited = [False] * num_nodes
    recursion_stack = [False] * num_nodes

    for node in range(1, num_nodes):
        if dfs(node):
            return True

    return False

inp = open("D:\CSE221\LAB ASSIGNMENT 4\input4.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output4.txt", "w") 
v,e = list(map(int, inp.readline().split()))
adj_list = {}
for i in range(1, v+1):
    adj_list[i] = []
for i in range(e):
    f,l,= list(map(int, inp.readline().split()))
    adj_list[f].append(l)
if has_cycle(adj_list):
    out.write("YES\n")
else:
    out.write("NO\n")
inp.close()
out.close()