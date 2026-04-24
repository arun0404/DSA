# Leetcode 1365

# nums = [8,1,2,2,3]
nums = [6,5,4,8]

class Solution:
    def smallerNumbers(self, nums):
        temp = sorted(nums)

        d = {}

        for i,num in enumerate(temp) :
            if num not in d:
                d[num] = i

        ret =[]
        for i in nums:
            ret.append(d[i])
        return ret

sol = Solution()
print(sol.smallerNumbers(nums))