'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
'''


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        ans = []
        while left <= right and top < bottom:
            print('---------')
            print('top is {}. bottom is {}'.format(top, bottom))
            for j in range(left, right + 1):
                ans.append(matrix[top][j])
            for i in range(top + 1, bottom):
                print('========')
                print(i, right)
                ans.append(matrix[i][right])
            for j in reversed(range(left, right + 1)):
                if top < bottom:
                    ans.append(matrix[bottom][j])
            for i in reversed(range(top + 1, bottom)):
                if left < right:
                    ans.append(matrix[i][left])
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return ans


if __name__ == '__main__':
    solution = Solution()
    matrix = [[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20]]
    print(solution.spiralOrder(matrix))