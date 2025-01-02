def mergeSort(arr, temp_arr, left, right):
    count = 0
    if left < right:  
        mid = (left + right)//2 
        count += mergeSort(arr, temp_arr, left, mid) 
        count += mergeSort(arr, temp_arr, mid + 1, right)
        count += merge(arr, temp_arr,  left, mid, right)
    return count
def merge(arr, temp_arr, left, mid, right):
    i = left     
    j = mid + 1 
    k = left     
    count = 0
    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            temp_arr[k] = arr[j]
            count += (mid-i + 1)
            k += 1
            j += 1
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]  
    return count
inp = open("D:\CSE221\LAB ASSIGNMENT 3\input1.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 3\output1.txt", "w")
n = int(inp.readline())
list = list(map(int, inp.readline().split()))
tempList = [0]*len(list)
result = mergeSort(list,tempList,0,len(list)-1)
out.write(str(result)+"\n")
inp.close()
out.close()