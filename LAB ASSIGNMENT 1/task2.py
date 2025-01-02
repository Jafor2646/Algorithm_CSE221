def bubbleSort(arr):
    flag = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break

inp = open("D:\CSE221\LAB ASSIGNMENT 1\input2.txt",'r')
out = open("D:\CSE221\LAB ASSIGNMENT 1\output2.txt",'w')
n = int(inp.readline())
arr = list(map(int,inp.readline().split()))
bubbleSort(arr)
output = ""
for i in range(n):
    if i!=n-1:
        output+= f"{arr[i]} "
    else:
        output+= str(arr[i])
out.write(output)
inp.close()
out.close()

# I achived theta(n) for best-case by simply adding a boolean flag variable.
# This variable keeps track if my inner loop swapped any value at all.
# If the input array is already swapped then inner loop will not swap any variable.
# My flag variable will keep track of previous inner iteration if it swapped any two value.
# if it swapped then I can assume the array is not sorted yet.
# if it did not swapped any two variable, then it is confirm that my array is sorted.