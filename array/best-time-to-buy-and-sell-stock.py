#!/usr/bin/python3

#best time to buy and sell stock
def maxProfit(prices):
    if len(prices) == 0:
        return 0
    max_profit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i - 1]:
            max_profit += prices[i] - prices[i - 1]
    return max_profit

def test_max_profit():
    assert maxProfit([7, 1, 5, 3, 6, 4]) == 7
    assert maxProfit([1, 2, 3, 4, 5]) == 4
    assert maxProfit([7, 6, 4, 3, 1]) == 0

#time complexity: O(n)
#space complexity: O(1)

if __name__ == '__main__':
    test_max_profit()