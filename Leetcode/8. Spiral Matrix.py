# Leetcode 54

# matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

class Solution():
    def spiralMatrix(self, matrix):
        res = []
        while matrix:
            # 1) add first row/list of matrix
            res += matrix.pop(0)

            # 2) append last element of all lists in order
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())

            # 3) add reverse of last row/list
            if matrix:
                res += matrix.pop()[::-1]

            # 4) append first element of all rows/elements in reverse
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))

        return res
    # print(spiralMatrix())
sol = Solution()
print(sol.spiralMatrix(matrix))