class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0: return 0
        prev = nums[0]
        seq,maxi = 1,0
        for i in range(len(nums)):
            if nums[i]==prev:
                pass
            elif nums[i] == prev+1:
                seq+=1
                prev=nums[i]
            else:
                seq=1
                prev=nums[i]
            if seq>maxi:
                    maxi=seq
        return maxi