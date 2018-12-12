'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
'''


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        index = 1
        matrix = [[0 for x in range(0, n)] for y in range(0, n)]
        left, right, top, bottom = 0, n - 1, 0, n - 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                matrix[top][i] = index
                index += 1
            for j in range(top + 1, bottom):
                matrix[j][right] = index
                index += 1
            for i in reversed(range(left, right + 1)):
                if top < bottom:
                    matrix[bottom][i] = index
                    index += 1
            for j in reversed(range(top + 1, bottom)):
                if left < right:
                    matrix[j][left] = index
                    index += 1
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return matrix


if __name__ == '__main__':
    solution = Solution()
    n = 4
    print(solution.generateMatrix(n))