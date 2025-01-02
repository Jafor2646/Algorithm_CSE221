def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])
  (array[i + 1], array[high]) = (array[high], array[i + 1])
  return i + 1
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quickSort(array, low, pi - 1)
    quickSort(array, pi + 1, high)
inp = open("D:\CSE221\LAB ASSIGNMENT 3\input3.txt", "r")
out = open("D:\CSE221\LAB ASSIGNMENT 3\output3.txt", "w")
n = int(inp.readline())
list = list(map(int, inp.readline().split()))
quickSort(list, 0, len(list)-1)
list = " ".join(str(item) for item in list)
out.write(list+"\n")
inp.close()
out.close()