class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = {}
        for num in nums:
            if num not in numbers:
                numbers[num] = 1
            else:
                numbers[num] += 1
        
        arr = []
        for num, cnt in numbers.items():
            arr.append([cnt,num])
        arr.sort()

        ans = []
        while len(ans) <k:
            ans.append(arr.pop()[1])
        return ans
            

        
