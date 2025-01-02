def stair(n, dp):
    if dp[n-1] != -1:
        return dp[n-1]
    if n == 0 or n == 1 :
        return 1
    dp[n-1] = stair(n-1, dp) + stair(n-2, dp)
    return dp[n-1]
inp = open("D:\CSE221\LAB ASSIGNMENT 8\input2.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 8\output2.txt","w")
n = int(inp.readline())
dp = [-1]*(n)
out.write(str(stair(n, dp)))
inp.close()
out.close()