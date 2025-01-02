def dfs(lst, i, j, visit, r, c, max):
    count = 0
    m1 = max
    visit[i][j] = 1
    if lst[i][j] == 'D':
        count += 1
    if lst[i][j] != '#':
        if i >= 0 and i < r-1:
            if visit[i+1][j] == 0:
                count += dfs(lst, i+1, j, visit, r, c, m1)
        if  i>0 and i < r:
            if visit[i-1][j] == 0:
              count += dfs(lst, i-1,j,visit,r,c,m1)
        if j >=0 and j < c-1:
            if visit[i][j+1] == 0:
                count += dfs(lst, i, j+1, visit, r, c, m1)
        if j > 0 and j < c:
            if visit[i][j-1] == 0:
                count += dfs(lst, i, j-1, visit, r, c, m1)
    if count > m1:
        m1 = count
    return m1
inp = open("D:\CSE221\LAB ASSIGNMENT 4\input6.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output6.txt", "w")
r, c = list(map(int, inp.readline().split()))
adj_mat = []
for i in range(r):
    inp1 = inp.readline()
    lst = []
    for j in inp1:
        lst.append(j)
    adj_mat.append(lst)
visited = []
for i in range(r):
    temp = []
    for j in range(c):
        temp.append(0)
    visited.append(temp)
m = dfs(adj_mat, 0, 0, visited, r, c, 0)
max = m
for i in range(r):
    for j in range(c):
        if(visited[i][j] == 0):
            m = dfs(adj_mat, i, j, visited, r, c, 0)
        if max < m:
            max = m       
out.write(str(max)+"\n")
inp.close()
out.close()