class Solution:
    def findComplement(self, num: int) -> int:
        output_str = ''
        for i in bin(num).replace('0b', ''):
            if i == '0':
                output_str += '1'
            else:
                output_str += '0'
        return int(output_str, 2)
