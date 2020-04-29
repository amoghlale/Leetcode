class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        final_list = [[1], [1, 1]]
        if rowIndex == 0:
            return final_list[0]
        elif rowIndex == 1:
            return final_list[1]
        else:
            for i in range(2, rowIndex+1):
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
            return final_list[-1]
