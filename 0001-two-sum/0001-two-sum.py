class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for i in range (len(nums)):
            hashmap[nums[i]] = i
        for i in range (len(nums)): 
            x = target - nums[i]
            if x in hashmap and hashmap[x] != i:
                return[i, hashmap[x]]