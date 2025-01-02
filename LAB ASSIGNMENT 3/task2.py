def DivAndCon(arr):
    if len(arr) <= 1:
        return float("-inf")
    if len(arr) == 2:
        return arr[0]+(arr[1]*arr[1])
    mid = len(arr)//2
    left_max = DivAndCon(arr[:mid])
    right_max = DivAndCon(arr[mid:])
    max1 = arr[0]
    for i in range(mid):
        if arr[i] > max1:
            max1 = arr[i]
    max2 = abs(arr[mid])
    for i in range(mid,len(arr)):
        if abs(arr[i]) > max2:
            max2 = abs(arr[i])
    cross_max = max1 + (max2*max2)
    if cross_max > left_max and cross_max>right_max:
        return cross_max
    elif left_max > cross_max and left_max > right_max:
        return left_max
    return right_max
inp = open("D:\CSE221\LAB ASSIGNMENT 3\input2.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 3\outpu2.txt", "w")
n = int(inp.readline())
list = list(map(int, inp.readline().split()))
#list = [9, 6, 5, 8, 2]
#list = [5, 10, 4, -3, 1, 6, -10, 2]
#list = [-4,3,2]
# i, j = 0, len(list)-1
# max = abs(list[1])
# maxIdx = 1
# for i in range(1,len(list)):
#     if(abs(list[i])>max):
#         max = abs(list[i])
#         maxIdx = i
# smax = list[0]
# for i in range(maxIdx):
#     if list[i] > smax:
#         smax = list[i]
# print(smax + (max*max))
result = DivAndCon(list)
out.write(str(result)+"\n")
inp.close()
out.close()