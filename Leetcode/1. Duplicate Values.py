# Leetcode 217

# class Solution:
    # def containDuplicate(self, nums: List(int))

# nums = input("nums = ").split(',')
nums = [1,2,3,1]  # True
# nums = [1,2,3,4]  # False

class Solution:
    def containDuplicate():
        if len(set(nums)) == len(nums):
            return False
        else:
            return True
        
    def containDuplicateAdvanced1(self, nums):
        return True if len(set(nums)) != len(nums) else False
    def containDuplicateAdvanced2(self, nums):
        return len(nums) != len(set(nums))
    
    print(containDuplicate())

sol = Solution()
print(sol.containDuplicateAdvanced1(nums))
print(sol.containDuplicateAdvanced2(nums))