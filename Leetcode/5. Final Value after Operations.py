# Leetcode 2011

# operations = ["--X","X++","X++"]  # 1
operations = ["++X","++X","X++"]  # 3

class Solution:
    def finalValue(self, operations) -> int:
        x = 0
        for i in operations:
            if "-" not in i:
                x +=1
            else:
                x=x-1
        return x
    
    def finalValueAdvanced(self, operations):
        x=0
        for i in operations:
            x += 1 if i[1] == '+' else -1
        return x

sol = Solution()
print(sol.finalValue(operations))
print(sol.finalValueAdvanced(operations))