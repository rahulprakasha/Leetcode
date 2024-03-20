class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numList = {}

        for i in range(len(nums)):
            if target - nums[i] in numList:
                return [i, numList[target-nums[i]]]
            numList[nums[i]] = i
        
