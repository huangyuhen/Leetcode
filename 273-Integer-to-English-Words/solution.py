class Solution(object):
    def __init__(self):
        self.LESS_THAN_TWENTY = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven",
                            "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        self.TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        self.THOUSANDS = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
            
        i = 0
        words = ""
        while num > 0:
            if num % 1000 != 0:
                words = self.helper(num % 1000) + self.THOUSANDS[i] + " " + words
            num /= 1000
            i += 1
        return words.rstrip()

    def helper(self, num):
        if num == 0:
            return ""
        elif num < 20:
            return self.LESS_THAN_TWENTY[num] + " "
        elif num < 100:
            return self.TENS[num / 10] + " " + self.helper(num % 10)
        else:
            return self.LESS_THAN_TWENTY[num / 100] + " Hundred " + self.helper(num % 100)