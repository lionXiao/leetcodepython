import sys


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        diff = sys.maxsize
        result = 0
        for index, a in enumerate(nums):
            l = index + 1
            r = len(nums) - 1
            while l < r:
                b, c = nums[l], nums[r]
                total = a + b + c
                if total == target:
                    return result
                if abs(target - total) < diff:
                    result = total
                    diff = abs(target - total)
                if total < target:
                    l += 1
                elif total > target:
                    r -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 2]
    print(solution.threeSumClosest(nums, 100))