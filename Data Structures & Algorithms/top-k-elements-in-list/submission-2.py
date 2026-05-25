class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numbers = Counter(nums)
        ans = []
        for num in numbers.most_common(k):
            ans.append(num[0])
        return ans
