inp = open("D:\CSE221\LAB ASSIGNMENT 2\input2b.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 2\output2b.txt", "w")
n = int(inp.readline())
lst1 = list(map(int, inp.readline().split())) 
m = int(inp.readline())
lst2 = list(map(int, inp.readline().split()))
lst =[0]*(n+m)
i, j , k= 0, 0, 0
while(i<n and j < m):
    if(lst1[i] <= lst2[j]):
        lst[k] = lst1[i]
        i += 1
        k += 1
    else:
        lst[k] = lst2[j]
        j += 1
        k += 1
while(i < n):
    lst[k] = lst1[i]
    i += 1
    k += 1
while(j < m):
    lst[k] = lst2[j]
    j += 1
    k += 1
out.write(str(lst)[1:-1]+"\n")
inp.close()
out.close()