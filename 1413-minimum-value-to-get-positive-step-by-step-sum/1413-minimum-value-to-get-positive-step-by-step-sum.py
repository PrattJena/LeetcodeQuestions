class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)):
            prefix.append(nums[i] + prefix[-1])
        
        minimum_value = min(prefix)
        if minimum_value <= 0:
            startValue = (minimum_value * -1) + 1
        else:
            startValue = 1
        
        return startValue