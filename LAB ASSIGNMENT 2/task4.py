def maxValue(arr):
    if len(arr) == 1:
        return arr[0]
    mid = len(arr)//2
    a1 = maxValue(arr[:mid])
    a2 = maxValue(arr[mid:])
    if(a1>a2):
        return a1
    return a2
inp = open("D:\CSE221\LAB ASSIGNMENT 2\input4.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 2\output4.txt", "w")
x = int(inp.readline())
lst = list(map(int, inp.readline().split()))
max = maxValue(lst)
out.write(str(max)+"\n")
inp.close()
out.close()
#time complexity is O(logn)