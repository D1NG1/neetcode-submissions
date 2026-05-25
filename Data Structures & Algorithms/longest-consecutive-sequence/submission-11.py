class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        nums_set = set()
        for num in nums:
            nums_set.add(num)

        current_count = 1
        largest_count = 1

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_count = 1
                while current_num + 1 in nums_set:
                    current_num += 1
                    current_count += 1
                largest_count = max(current_count, largest_count)
                
        return largest_count