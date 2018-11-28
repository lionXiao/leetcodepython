'''Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
'''


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        subres = []

        def DFS(nums, subres, idx):
            if idx == len(nums):
                self.res.append(subres[:])
                return
            subres.append(nums[idx])
            DFS(nums, subres, idx+1)
            subres.pop()
            DFS(nums, subres, idx+1)
        DFS(nums, subres, 0)
        return self.res




if __name__ == '__main__':
    nums = [1, 2, 3]
    solution = Solution()
    print(solution.subsets(nums))