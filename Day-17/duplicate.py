#leetcode problem
class Solution:
    def containsNearbyDuplicate(self, nums,k):
        map={}
        for i in range(len(nums)):
            if nums[i] in map:
                if abs(i-map[nums[i]])<=k:
                    return True
            map[nums[i]]=i
        return False