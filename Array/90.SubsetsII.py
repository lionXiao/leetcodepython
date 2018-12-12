'''
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        subres = []
        nums.sort()
        def DFS(nums, subres, idx):
            if idx == len(nums):
                if subres[:] not in self.res:
                    self.res.append(subres[:])
                return
            subres.append(nums[idx])
            DFS(nums, subres, idx + 1)
            subres.pop()
            DFS(nums, subres, idx + 1)

        DFS(nums, subres, 0)
        return self.res



if __name__ == '__main__':
    nums = [4, 4, 4, 1, 4]
    solution = Solution()
    print(solution.subsetsWithDup(nums))