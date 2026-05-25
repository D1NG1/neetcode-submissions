class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        sort_nums = sorted(nums)
        count = 1
        largest_count = 0
        current = sort_nums[0]
        for i in range(1,len(sort_nums)):
            if sort_nums[i] == (current+1):
                count += 1
            elif sort_nums[i] == current:
                continue
            else:  
                largest_count = max(count,largest_count)
                count = 1
            current = sort_nums[i]
        largest_count = max(count,largest_count)
        return largest_count
        