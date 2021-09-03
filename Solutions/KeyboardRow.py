class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        top = set('qwertyuiop')
        middle = set('asdfghjkl')
        bottom = set('zxcvbnm')
        output_list = []
        for word in words:
            set_of_word = set(word.lower())
            if set_of_word.issubset(top) or set_of_word.issubset(middle) or set_of_word.issubset(bottom):
                output_list.append(word)
        return output_list
