class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        res = 0
        for num in nums:
            s.add(num)
        for num in nums:
            if num -1 in s:
                continue
            cnt = 0
            while num in s:
                cnt += 1
                num += 1
            res = max(res,cnt)
        return res 