inp = open("inputa1.txt", 'r')
path = "output1a.txt"
out = open(path, 'w')
t = int(inp.readline())
for i in range(t):
  x = int(inp.readline())
  if( x%2 == 0):
    temp = f"{x} is an Even number.\n"
    out.write(temp)
  else:
    temp = f"{x} is an Odd number.\n"
    out.write(temp)
inp.close()
out.close()