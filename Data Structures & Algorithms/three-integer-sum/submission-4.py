class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        ans = []
        print(nums)
        for i,n in enumerate(nums):
            j = i+1
            k = len(nums)-1
            while j < k:
                if n + nums[j]+ nums[k]>0:
                    k-=1
                elif n + nums[j]+ nums[k]<0:
                    j+=1
                else:
                    if [n,nums[j],nums[k]] not in ans:
                        ans.append([n,nums[j],nums[k]]) 
                    j +=1
                    k -=1
        return ans

