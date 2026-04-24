# Leetcode 1 

nums = [2,11,7,15]
target = 13

class Solution:
    def twoSum():
        hashmap = {} #val, indx

        for index, value in enumerate(nums):
            # diff = target - value
            if target-value in hashmap:
                # return index, hashmap[target-value]
                return hashmap[target-value], index
            hashmap[value] = index
            
    print(twoSum())
            