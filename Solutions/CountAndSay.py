class Solution(object):
    def count_consecutive(self, num):
        i = 0
        j = 1
        count = 1
        output_num = ""
        while i < len(num)+1:
            if j >= len(num) and i <= len(num)-1:
                output_num += str(count) + num[i]
                break
            if num[i] == num[j]:
                count += 1
                j += 1
            else:
                output_num += str(count) + num[i]
                i = j
                j += 1
                count = 1
        return output_num

    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        first_val = "1"
        if n == 1:
            return first_val
        else:
            for i in range(n-1):
                output_num = self.count_consecutive(first_val)
                first_val = output_num
            return output_num
