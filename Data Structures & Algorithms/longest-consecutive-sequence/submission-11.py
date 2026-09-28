class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if nums == []:
            return 0
        nums.sort()
        print(nums)


        max_len = 1
        cur_length = 1

        for i in range(len(nums) - 1):

            if nums[i] == nums[i+1]:
                continue
            
            if nums[i] + 1 == nums[i+1]:
                cur_length+=1
            else:
                cur_length = 1
            
            if cur_length > max_len:
                max_len = cur_length
            
        return max_len