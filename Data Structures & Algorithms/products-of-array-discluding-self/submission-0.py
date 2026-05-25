class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = []

        for i in range(len(nums)):
            current = 1
            for j in range(len(nums)):
                if i ==j:
                    continue
                else:
                    current *= nums[j]
            ans.append(current)
        return ans