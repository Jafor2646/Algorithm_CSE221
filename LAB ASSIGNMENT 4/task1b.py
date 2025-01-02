inp = open("D:\CSE221\LAB ASSIGNMENT 4\input1b.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 4\output1b.txt", "w")
v,e = list(map(int, inp.readline().split()))
adj_list = [[] for i in range(v+1)]
for i in range(e):
    f,l,w = list(map(int, inp.readline().split()))
    adj_list[f].append((l,w))
for i in range(v+1):
    out.write(str(i)+" : "+ " ".join(str(item) for item in adj_list[i])+"\n")
inp.close()
out.close()