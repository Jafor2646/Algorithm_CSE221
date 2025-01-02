class Node:
    def __init__(self,studentID,mark):
        self.studentID = studentID
        self.mark = mark

def bubbleSort(arr:list[Node]):
    for i in range(len(arr)-1):
        didChange = False
        for j in range(len(arr)-i-1):
            if arr[j].mark < arr[j+1].mark:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                didChange = True
            if(arr[j].mark==arr[j+1].mark):
                if arr[j].studentID > arr[j+1].studentID:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    didChange = True
        if didChange == False:
            break

input3 = open("D:\CSE221\LAB ASSIGNMENT 1\input3.txt", 'r')
output = open("D:\CSE221\LAB ASSIGNMENT 1\output3.txt",'w')
t = int(input3.readline())
si = list(map(int,input3.readline().split()))
sm = list(map(int,input3.readline().split()))
myNode=list()
for i in range(t):
    currentNode = Node(si[i],sm[i])
    myNode.append(currentNode)
bubbleSort(myNode)
for i in range(t):
    if i!=t-1:
        output.write(f'ID: {myNode[i].studentID} Mark: {myNode[i].mark}\n')
    else:
        output.write(f'ID: {myNode[i].studentID} Mark: {myNode[i].mark}')
input3.close()
output.close()