Solution 1:
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return num % 9 if num % 9 !=0 else 9

Solution 2:
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            num = sum(map(int, [i for i in str(num)]))
        return num
