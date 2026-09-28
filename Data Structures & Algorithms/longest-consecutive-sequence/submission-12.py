class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        st = set(nums)
        res = 0
        for num in st:
            if num-1 in st:
                continue
            cnt = 1
            while num+1 in st:
                num = num+1
                cnt += 1
            res = max(res, cnt)
        return res