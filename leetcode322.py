class Solution:
    def coinChange(self, coins, amount: int):
        if amount == 0:
            return 0
        if amount<min(coins):
            return -1
        coins = list(filter(lambda x:x<=amount,coins))
        dp = [float('inf')]*(amount+1)
        for coin in coins:
            dp[coin]=1
        for i in range(min(coins)+1, amount+1):
            tmp = [dp[i]]
            for coin in coins:
                if i-coin>0:
                    tmp.append(dp[i-coin]+1)
            dp[i]=min(tmp)
        if dp[amount]==float('inf'):
            return -1
        return dp[amount]

if __name__ =='__main__':
    input = [1,2, 5]
    entity = Solution()
    print(entity.coinChange(input,10))