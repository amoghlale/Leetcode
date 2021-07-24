class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1.zfill(max(len(num1), len(num2)))
        num2 = num2.zfill(max(len(num1), len(num2)))
        carry = 0
        output = ''
        for i in range(len(num1) - 1, -1, -1):
            x = ord(num1[i]) - ord('0')
            y = ord(num2[i]) - ord('0')
            added_result = x + y + carry
            if added_result > 9:
                output += str(added_result % 10)
                carry = added_result // 10
            else:
                output += str(added_result)
                carry = 0
        if carry != 0:
            output += str(carry)
        return output[::-1]
