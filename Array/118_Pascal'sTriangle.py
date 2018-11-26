'''Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.'''
'''In Pascal's triangle, each number is the sum of the two numbers directly above it.'''
'''
Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]'''


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle_arr = []
        for i in range(numRows):
            temp = [1] * (i + 1)
            triangle_arr.append(temp)
            for j in range(1, i):
                triangle_arr[i][j] = triangle_arr[i - 1][j - 1] + triangle_arr[i - 1][j]
        return triangle_arr


if __name__ == '__main__':
    numRows = 10
    solution = Solution()
    print(solution.generate(numRows=numRows))