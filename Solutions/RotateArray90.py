class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        """
        0,0=0,2
        0,2=2,2
        2,2=2,0
        2,0=0,0
        1,0=0,1
        0,1=1,2
        1,2=2,1
        2,1=1,0
        1,1=1,1
        """
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                # transpose matrix
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
            # convert [1,4,7] to [7,4,1]
            matrix[row] = matrix[row][::-1]
        return matrix
