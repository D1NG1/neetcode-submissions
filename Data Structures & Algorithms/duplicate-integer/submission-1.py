class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = len(nums) - 1
        while i > 0:
            current = nums.pop(i)
            print(current)
            if current in nums:
                return True
            i = i-1
        return False

