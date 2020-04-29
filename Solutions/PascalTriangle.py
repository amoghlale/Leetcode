class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            final_list = [[1], [1, 1]]
            for i in range(2, numRows):
                previous = final_list[-1]
                i = 0
                j = 1
                current = [1]
                while i < len(previous) and j < len(previous):
                    current.append(previous[i] + previous[j])
                    i += 1
                    j += 1
                current.append(1)
                final_list.append(current)
            return final_list
