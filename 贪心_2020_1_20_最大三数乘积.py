class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        min1, min2 = [float('inf')] * 2  # 两个负数最小值
        max1, max2, max3 = [float('-inf')] * 3  # 三个最大正数值
        for num in nums:
            min1, min2, _ = sorted([min1, min2, num])
            _, max1, max2, max3 = sorted([max1, max2, max3, num])
        return max(min1 * min2 * max3, max1 * max2 * max3)
