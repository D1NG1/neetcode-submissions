class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if (target - nums[i]) in nums[1:]:
                idx = nums.index(target - nums[i])
                if i !=idx:
                    ans = [i,idx]
                    ans = sorted(ans)
                    return ans

            
