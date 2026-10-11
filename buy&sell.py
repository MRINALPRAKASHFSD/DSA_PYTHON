class Solution:
    def maxProfit(self, prices:list[int]) -> int:
        l, r = 0, 1
        maxP = 0
       
       
        while r < len(prices):
            if prices[l]< prices[r]:
               profit = prices[r] - prices[l]
               maxP= max(maxP ,profit)  
            else:
             l = r 
            r+=1
 # O(n) time complexity and O(1) space complexity 