class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = [i for i in s if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')]
        if len(vowels) == 0:
            return s
        else:
            correct_order_of_vowels = vowels[::-1]
            j = 0
            output_str = ""
            for i in s:
                if i in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
                    output_str += correct_order_of_vowels[j]
                    j += 1
                else:
                    output_str += i
            return output_str
