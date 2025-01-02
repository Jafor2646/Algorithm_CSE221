def split(lst):
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]
    return left, right
def merge(left, right):
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i += 1
    while j < len(right):
        l.append(right[j])
        j+=1
    return l
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    left_half, right_half = split(lst)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)
inp = open("D:\CSE221\LAB ASSIGNMENT 2\input2a.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 2\output2a.txt", "w")
n = int(inp.readline())
lst1 = list(map(int, inp.readline().split())) 
m = int(inp.readline())
lst2 = list(map(int, inp.readline().split()))
lst = lst1 + lst2
lst = merge_sort(lst)
out.write(str(lst)[1:-1]+"\n")
inp.close()
out.close()