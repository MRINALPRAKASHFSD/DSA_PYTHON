class Solution:
    def arrayPartition(self, nums:list[int]) -> int:
        nums.sort()
        return sum(nums[::2 ]) # O(nlogn) time complexity and O(1) space complexity