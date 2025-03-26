# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]

def buy_Sell(prices):
    max_profit = 0
    for i in range(0,len(prices)):
        price = 0
        for j in range(i+1,len(prices)):
            profit = prices[j]-prices[i]
            max_profit = max(profit,max_profit)
    print(max_profit)

buy_Sell(prices)




