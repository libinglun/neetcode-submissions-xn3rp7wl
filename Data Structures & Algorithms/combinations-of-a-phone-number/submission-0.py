class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        self.string = ''
        def dfs(i):
            if i == len(digits):
                res.append(self.string)
                return 
            
            for char in digitToChar[digits[i]]:
                self.string += char
                dfs(i + 1)
                self.string = self.string[:-1]

        dfs(0)
        return res
