inp = open("D:\CSE221\LAB ASSIGNMENT 4\input1a.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output1a.txt", "w")
v,e = list(map(int, inp.readline().split()))
adj_mat = [[0 for i in range(v+1)]for j in range(v+1)]
for i in range(e):
    f,l,w = list(map(int, inp.readline().split()))
    adj_mat[f][l] = w
for i in range(v+1):
    out.write((" ".join(str(item) for item in adj_mat[i]))+"\n")
inp.close()
out.close()