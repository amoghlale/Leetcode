class Solution(object):
    def group_anagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        map_dict = {}
        for str_val in strs:
            sorted_str = ''.join(sorted(str_val))
            if sorted_str in map_dict:
                map_dict[str(sorted_str)].append(str(str_val))
            else:
                map_dict[str(sorted_str)] = [str(str_val)]
        return list(map_dict.values())
