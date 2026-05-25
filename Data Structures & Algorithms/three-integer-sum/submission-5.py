class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i >0 and nums[i-1]==n:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                if n + nums[j]+ nums[k]>0:
                    k-=1
                elif n + nums[j]+ nums[k]<0:
                    j+=1
                else:
                    ans.append([n,nums[j],nums[k]]) 
                    j +=1
                    k -=1
                    while nums[j]==nums[j-1] and j < k:
                        j+=1
        return ans

