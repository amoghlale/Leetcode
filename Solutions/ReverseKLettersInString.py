class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        slices_of_2k = [s[i:i + 2*k] for i in range(0, len(s), 2*k)]
        expected_output = []
        for i in slices_of_2k:
            if len(i) < k:
                expected_output.append(i[::-1])
            else:
                expected_output.append(i[k-1::-1] + i[k::])
        return ''.join(expected_output)
