def max_profit(prices):
    total_profit = 0  
    for i in range(1, len(prices)):  
        if prices[i] > prices[i - 1]:
            total_profit += prices[i] - prices[i - 1]
    
    return total_profit 
prices1 = [7, 1, 5, 3, 6, 4]
print(max_profit(prices1))  

prices2 = [1, 2, 3, 4, 5]
print(max_profit(prices2))  

prices3 = [7, 6, 4, 3, 1]
print(max_profit(prices3))  
