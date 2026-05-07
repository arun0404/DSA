# Leetcode 1266
# Chebyshev distance - a measure of distance between two points defined as the maximum absolute difference between their coordinates.
#It is most commonly known as chessboard distance

points = [[1,1],[3,4],[-1,0]]
# points = [[3,2],[-2,2]]

class Solution():
    def minimumTimeVisiting(self, points):
        res=0
        x1,y1 = points.pop()
        while points:
            x2,y2 = points.pop()
            res += max(abs(x2-x1), abs(y2-y1))
            x1,y1 = x2,y2
        return res

sol = Solution()
print(sol.minimumTimeVisiting(points))
