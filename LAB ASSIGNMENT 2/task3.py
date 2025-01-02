def merge(a, b):
    l = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i]<b[j]:
            l.append(a[i])
            i += 1
        else:
            l.append(b[j])
            j += 1
    while i < len(a):
        l.append(a[i])
        i += 1
    while j < len(b):
        l.append(b[j])
        j+=1
    return l
def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    a1 = mergesort(arr[:mid])
    a2 = mergesort(arr[mid:])
    return merge(a1, a2)
inp = open("D:\CSE221\LAB ASSIGNMENT 2\input3.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 2\output3.txt", "w")
n = int(inp.readline())
lst = list(map(int, inp.readline().split()))
lst = mergesort(lst)
out.write(str(lst)[1:-1]+"\n")
inp.close()
out.close()