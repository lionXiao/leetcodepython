"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
keyMap = {
    "0": " ",
    "1": "*",
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}
"""
"""
Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

"""
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.
"""

from functools import reduce

class solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        keyMap = {
            "0": " ",
            "1": "*",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        return reduce(lambda results, digit: [result + letter for result in results for letter in keyMap[digit]], digits, [''])


if __name__ == '__main__':
    solu = solution()
    print(solu.letterCombinations('23'))