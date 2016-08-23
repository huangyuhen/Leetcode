class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        if not digits:
            return []
        results = [""]
        dict = {"1": "", "2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        for digit in digits:
            if digit == "1":
                continue
            word = dict[digit]
            temp = []
            for i in word:
                for result in results:
                    temp.append(result + i)
            results = temp
        return results