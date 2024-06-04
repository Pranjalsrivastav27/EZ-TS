#leetcode problem
class Solution:
    def productExceptSelf(self, nums):
        pro=1
        zero=0
        count=0
        result=[]
        for i in nums:
            if i==0:
                zero=1
                count=count+1
                continue
            else:
                pro=pro*i
        if count>1:
            pro=0
        if zero:
            for i in nums:
                if i==0:
                    result.append(pro)
                    continue
                result.append(0)
        else:
            for i in nums:
                result.append(int(pro/i))
        return result