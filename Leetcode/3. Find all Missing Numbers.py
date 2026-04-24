# Leetcode 448


# nums = input().split(',')
nums  = [4,3,2,7,8,2,3,1]

class Solution:
    def findMissingNumbers():
        list = []
        set_num = set(nums)

        for i in range(1, len(nums)+1):
            if i not in set_num:
                list.append(i)
        return list
    
    print(findMissingNumbers())

    # Advanced Solution
    def findMissingNumberAdvanced():
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
        res = []
        for index, number in enumerate(nums):
            if number > 0:
                res.append(index+1)
        return res
    print(findMissingNumberAdvanced())