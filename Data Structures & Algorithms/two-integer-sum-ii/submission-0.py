class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for index,num in enumerate(numbers):
            complement = target - num
            if complement in seen:
                return [seen[complement],index+1]
            seen[num]=index+1