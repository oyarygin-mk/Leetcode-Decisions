# Brute force 0 (n**2)
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) < 2:
            return 0

        n = len(prices)
        deals = []
        for i in range(n):
            for j in range(i + 1, n):
                deals.append(prices[j] - prices[i])
        return max(max(deals), 0)

if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(Solution().maxProfit(prices))
