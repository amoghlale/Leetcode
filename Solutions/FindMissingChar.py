class Solution:
    def calculate_sum(self, stringName):
        sum_of_sn = 0
        for c in stringName:
            sum_of_sn += ord(c)
        return sum_of_sn

    def findTheDifference(self, s: str, t: str) -> str:
        if len(s) == 0 and len(t) == 1:
            return t[0]
        else:
            return chr(self.calculate_sum(t) - self.calculate_sum(s))
