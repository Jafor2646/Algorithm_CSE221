inp = open("D:\CSE221\LAB ASSIGNMENT 2\input1b.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 2\output1b.txt", "w")
n,k = list(map(int, inp.readline().split()))
lst = list(map(int, inp.readline().split()))
dic1 = dict()
ans = ""
for i in range(n):
    if lst[i] in dic1:
        dic1[lst[i]].append(i)
    else:
        dic1[lst[i]] = [i]
for key,v in dic1.items():
    if (k-key) in dic1:
        ans += (str(v[0]+1)+" ")
        if(key == (k-key)):
            ans += str(dic1[k-key][1]+1)
        else:
            ans += str(dic1[k-key][0]+1)
        break
if len(ans) == 0:
    out.write("IMPOSSIBLE\n")
else:
    out.write(ans+"\n")
inp.close()
out.close()
  
