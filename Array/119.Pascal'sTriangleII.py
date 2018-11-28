'''Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

Note that the row index starts from 0.'''
'''In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?'''


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = []
        nk = 1
        res.append(nk)
        for i in range(2, rowIndex + 2):
            nk = nk * (rowIndex + 1 - i + 1) / (i - 1)
            res.append(int(nk))
        return res


if __name__ == '__main__':
    numRows = 3
    solution = Solution()
    print(solution.getRow(rowIndex=numRows))