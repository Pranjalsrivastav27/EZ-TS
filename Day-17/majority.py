#leetcode problem
class Solution:
    def majorityElement(self, nums):
        n=len(nums)/3
        map={}
        a=[]
        for i in nums:
            if i in map:
                map[i]=map[i]+1
            else:
                map[i]=1
        for i in map:
            if map[i]>n:
                a.append(i)
        return a