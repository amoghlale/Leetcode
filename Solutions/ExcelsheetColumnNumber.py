from string import ascii_uppercase
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        alphabet_array = list(ascii_uppercase)
        ref_idx_list = [i for i in range(1, 27)]
        output_sum = 0
        len_column_title = len(columnTitle) - 1
        for i in columnTitle:
            output_sum += (ref_idx_list[alphabet_array.index(i)] * 26**len_column_title)
            len_column_title -= 1
        return output_sum
