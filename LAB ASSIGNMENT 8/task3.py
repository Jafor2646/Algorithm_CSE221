def coinChange(coins, amount, dp):
    if(amount == 0):
        return 0
    if amount < 0:
        return float("inf")
    if dp[amount] != -1:
        return dp[amount]
    mini = float("inf")
    for i in range(len(coins)):
        ans = coinChange(coins, amount-coins[i], dp)
        if(ans != float("inf")):
            mini = min(mini, 1+ans)
    dp[amount] = mini
    return dp[amount] 

inp = open("D:\CSE221\LAB ASSIGNMENT 8\input3.txt","r")
out = open("D:\CSE221\LAB ASSIGNMENT 8\output3.txt","w")
n, amount = list(map(int, inp.readline().split()))
coins = list(map(int, inp.readline().split()))
dp = [-1]*(amount+1)
out.write(str(coinChange(coins, amount, dp))+"\n")
inp.close()
out.close()