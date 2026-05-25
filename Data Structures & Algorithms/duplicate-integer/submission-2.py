class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for num in nums:
            count = 0
            for i in range(len(nums)):
                if num == nums[i]:
                    count+=1
            if count >=2 :
                return True
        return False