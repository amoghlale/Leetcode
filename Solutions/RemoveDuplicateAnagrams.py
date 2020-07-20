class Solution:
    def removeDuplicateAnagrams(self, ip: List) -> List:
        output_list = []
        output_list_with_sorted_char = []
        for i in range(len(ip)):
            for j in range(i+1, len(ip)):
                if sorted(ip[i]) != sorted(ip[j]):
                    if sorted(ip[i]) not in output_list_with_sorted_char:
                        if ip[i] not in output_list:
                            output_list.append(ip[i])
                        output_list_with_sorted_char.append(sorted(ip[i]))
                if sorted(ip[j]) not in output_list_with_sorted_char:
                    if ip[j] not in output_list:
                        output_list.append(ip[j])
                    output_list_with_sorted_char.append(sorted(ip[j]))
        return output_list
