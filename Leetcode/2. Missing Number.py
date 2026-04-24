# Leetcode 268

# Sorting in python is (N log N)

# nums = input().split(',')
nums = [0,2] # 1
# nums = [3,0,1]  # 2

class Solution:
    def missingNumbers(): # Sorting in python is (N log N)
        nums.sort()
        for index, value in enumerate(nums):
            if (index != value):
                return value-1
            if value == len(nums)-1:
                return value+1
    
    def missingNumbersOptimized():
        return sum(range(len(nums)+1)) - sum(nums)

    print(missingNumbers())
    print(missingNumbersOptimized())