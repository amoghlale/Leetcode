class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        pattern_char = [i for i in pattern]
        str_words = str.split()
        if len(pattern_char) == len(str_words):
            i = 0
            output_str = ""
            map_dict = {}
            while i < len(pattern_char):
                if pattern_char[i] not in map_dict and str_words[i] not in map_dict.values():
                    map_dict[pattern_char[i]] = str_words[i]
                i += 1
            for i in pattern:
                if i in map_dict:
                    output_str += map_dict[i] + " "
            return True if str == output_str[:-1] else False
