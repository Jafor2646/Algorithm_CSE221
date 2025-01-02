inp = open("D:\CSE221\LAB ASSIGNMENT 1\input1b.txt", 'r')
path = "D:\CSE221\LAB ASSIGNMENT 1/output1b.txt"
out = open(path, 'w')
t = int(inp.readline())
for i in range(t):
  temp = ""
  lst = inp.readline().split()
  if lst[2] == '+':
    x = int(lst[1]) + int(lst[3])
    temp = f"The result of {lst[1]} + {lst[3]} is {x}\n"
  elif lst[2] == '-':
    x = int(lst[1]) - int(lst[3])
    temp = f"The result of {lst[1]} - {lst[3]} is {x}\n"
  elif lst[2] == '*':
    x = int(lst[1]) * int(lst[3])
    temp = f"The result of {lst[1]} * {lst[3]} is {x}\n"
  elif lst[2] == '/':
    x = int(lst[1]) / int(lst[3])
    temp = f"The result of {lst[1]} / {lst[3]} is {x}\n"
  out.write(temp)
inp.close()
out.close()