from itertools import product
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        # min length "0000" = 4
        # max length "255255255255" = 12
        if len(s) < 4 or len(s) > 12:
            return []
        else:
            ip_list = []
            for split_length_combo in [i for i in list(product(range(1, 4), repeat=4)) if sum(i) == len(s)]:
                potentional_output_str = ""
                j = 0
                for eight_bit_val_length in split_length_combo:
                    if 0 <= int(s[j: j+eight_bit_val_length]) <= 255:
                        if len(str(s[j: j+eight_bit_val_length])) > 1:
                            potentional_output_str += str(s[j: j+eight_bit_val_length]).lstrip("0") + "."
                        else:
                            potentional_output_str += str(s[j: j+eight_bit_val_length]) + "."
                        j += eight_bit_val_length
                    else:
                        break
                if len(potentional_output_str) == len(s) + 4:
                    ip_list.append(potentional_output_str[:-1])
            return ip_list
