inp = open("D:\CSE221\LAB ASSIGNMENT 2\input1a.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 2\output1a.txt", "w")
n,k = list(map(int, inp.readline().split()))
lst = list(map(int, inp.readline().split()))
ans = ""
flag = False
for i in range(n-1):
    for j in range(i+1, n):
        if(lst[i]+lst[j] == k):
            ans += (str(i+1)+" ")
            ans += str(j+1)
            flag = True
            break
    if(flag):
        break
if(len(ans) == 0):
    out.write("IMPOSSIBLE\n")
else:
    out.write(ans+"\n")