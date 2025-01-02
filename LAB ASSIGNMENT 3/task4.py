def partition(x, l, r):
    pivot = x[r]
    i = l-1
    for j in range(l, r):
        if x[j] <= pivot:
            i = i+1
            (x[i], x[j]) = (x[j] , x[i])
    (x[i+1], x[r])= (x[r], x[i+1])
    return i+1
def kthsmallestArray(x, l, r ,k):
    if l == r:
        return x[l]
    pos = partition(x, l , r)
    i = pos - l + 1
    if i == k:
        return x[pos]
    elif i>k:
        return kthsmallestArray(x,l,pos-1, k)
    return kthsmallestArray(x, pos+1, r, k-i)
inp = open("D:\CSE221\LAB ASSIGNMENT 3\input4.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 3\output4.txt", "w")
x = int(inp.readline())
lst = list(map(int, inp.readline().split()))
k = int(inp.readline())
for i in range(k):
    a = int(inp.readline())
    num = kthsmallestArray(lst,0,len(lst)-1,a)
    out.write(str(num)+"\n")
inp.close()
out.close()
    
    