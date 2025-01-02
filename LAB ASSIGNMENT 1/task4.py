class Node:
    def __init__(self,string,name,time,position):
        self.string = string
        self.name = name
        self.time = time
        self.position = position

def bubbleSort(arr:list[Node]):
    flag = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i-1):
            if arr[j].name > arr[j+1].name:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
            if (arr[j].time<arr[j+1].time) and (arr[j].name == arr[j+1].name):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
            if (arr[j].position>arr[j+1].position) and (arr[j].name == arr[j+1].name) and (arr[j].time == arr[j+1].time):
                arr[j], arr[j+1] = arr[j+1], arr[j]
                flag = True
        if not flag:
            break
inp = open('D:\CSE221\LAB ASSIGNMENT 1\input4.txt','r')
out = open("D:\CSE221\LAB ASSIGNMENT 1\output4.txt",'w')
t = int(inp.readline())
arr: list[Node] = list()
for run in range(t):
    string = str(inp.readline())
    temp = list(map(str,string.split()))
    string = ' '.join(temp)
    name,_,_,_,_,_,time = temp
    h,m = list(map(int,time.split(':')))
    time = (h*60)+m
    currentNode = Node(string,name,time,run+1)
    arr.append(currentNode)
bubbleSort(arr)
for i in range(t):
    if i!=t-1:
        out.write(f'{arr[i].string}\n')
    else:
        out.write(f'{arr[i].string}')